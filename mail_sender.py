import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_mail_parts():
    with open('files/birthday_template') as file:
        title = file.readline()
        body = file.read()
        return title, body


def get_email():
    f = open("./files/email", "r")
    contents = f.read()
    f.close()
    return contents


def send_email(mail_content, receivers):
    topic, body = get_mail_parts()
    sender_address = get_email()
    sender_pass = os.getenv("PASSWORD")
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ", ".join(receivers)
    message['Subject'] = topic
    message.attach(MIMEText(body.format(mail_content), 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, ", ".join(receivers), text)
    session.quit()
    print('Mail Sent')


if __name__ == "__main__":
    send_email("Nigar Movsumova", ['movsum.nigar@gmail.com'])
