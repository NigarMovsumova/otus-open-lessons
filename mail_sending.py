import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from tkinter import messagebox

# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python


def change_email_address(new_email):
    f = open("email", "w")
    f.write(new_email)
    f.close()
    messagebox.showinfo("Success", "Email is changed to " + new_email)


def get_email():
    f = open("email", "r")
    contents = f.read()
    return contents


def send_email(mail_content):
    sender_address = get_email()
    sender_pass = os.environ['PASSWORD']
    receiver_address = 'movsum.nigar@gmail.com'
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
