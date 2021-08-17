import schedule
import time

from database import Notification, MailAddress
from mail_sender import send_email, get_mail_parts


def execute_job():
    # 1. Получить уведомления
    # 2. Получить все почтовые адреса
    # 3. Собрать темплейт
    # 4. Отправить почтовые сообщения
    notification = Notification()
    notification_cursor, notification_connection = notification.get_enabled_notifications(
        '2021-08-17')
    mail = MailAddress()
    mail_cursor, mail_connection = mail.get_emails()
    for (id, notification_type, topic, notification_date, created_at, updated_at, status) in notification_cursor:
        print(id, notification_type, topic, notification_date,
              created_at, updated_at, status)
        try:
            for (id, mail_address) in mail_cursor:
                print(topic, mail_address)
                send_email(topic, [mail_address])
        except BaseException as e:
            print(e)


schedule.every(7).seconds.do(execute_job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("11:50").do(execute_job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
