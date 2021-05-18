import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python


def send_email(mail_content):
    sender_address = 'otus.open.lesson@gmail.com'
    sender_pass = os.environ['PASSWORD']
    receiver_address = 'otus.open.lesson@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Price Notification by Trader App'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


send_email('Hello World!')
send_email('привет')
send_email('Прєвєд!')

