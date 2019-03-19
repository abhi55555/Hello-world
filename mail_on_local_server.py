import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
RECEIVER = os.environ.get('RECEIVER')

# To start a local debug server(in windows) -> python -m smtpd -c DebuggingServer -n localhost:1025

with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Sample email on local server'
    body = 'This mail is send by running simple python program'

    msg = f'Subject: {subject} \n\n {body}'

    smtp.sendmail(EMAIL_ADDRESS, RECEIVER, msg)
