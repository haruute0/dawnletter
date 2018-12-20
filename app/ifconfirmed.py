from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user

def check_confirmed(func):
    @wraps(func)
    def ifconfirmed(*args, **kwargs):
        if current_user.confirmed is False:
            return redirect(url_for('unconfirmed'))
        return func(*args, **kwargs)

    return ifconfirmed