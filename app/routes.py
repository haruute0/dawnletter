from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.token import generate_confirmation_token, confirm_token
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.email import send_email_sendgrid
from werkzeug.urls import url_parse
from app.ifconfirmed import check_confirmed

@app.route('/')
@app.route('/index')
@login_required
@check_confirmed
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)   
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            confirmed=False
            )
        user.set_uuid()
        user.set_password(form.password.data)
        user.get_time_stamp()

        token = generate_confirmation_token(form.email.data)

        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email_sendgrid(user.email, subject, html)

        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash('A confirmation email has been sent via email.', 'success')
        return redirect(url_for("unconfirmed"))
    return render_template('register.html', title='Register', form=form)

@app.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
        print(email)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.get_confirmed()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index'))

@app.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('index'))
    flash('Please confirm your account!', 'warning')
    return render_template('unconfirmed.html')

@app.route('/resend')
@login_required
def resend_email_confirmation():
    token = generate_confirmation_token(current_user.email)

    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email_sendgrid(current_user.email, subject, html)    
    
    flash('A new confirmation email has been sent.', 'success')

    return redirect(url_for('unconfirmed'))