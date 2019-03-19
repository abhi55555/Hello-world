import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
RECEIVER = os.environ.get('RECEIVER')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Sample email'
    body = 'This mail is send by running simple python program'

    msg = f'Subject: {subject} \n\n {body}'

    smtp.sendmail(EMAIL_ADDRESS, RECEIVER, msg)
