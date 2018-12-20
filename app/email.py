from config import Config
import sendgrid
from sendgrid.helpers.mail import *

def send_email_sendgrid(to, subject, template):
    sg = sendgrid.SendGridAPIClient(apikey=Config.SENDGRID_API_KEY)
    from_email = Email(Config.MAIL_DEFAULT_SENDER)
    to_email = Email([to])
    subject = subject
    content = Content("text/plain", template)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)