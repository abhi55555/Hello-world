import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
RECEIVER = os.environ.get('RECEIVER')

msg = EmailMessage()
msg['Subject'] = 'Hello friend'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECEIVER
msg.set_content('Hi, how are you')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
