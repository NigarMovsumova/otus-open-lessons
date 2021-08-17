import mysql.connector as connector
import datetime


class Database:
    def __init__(self):
        self.connection = connector.connect(
            host="db-mysql-fra1-43035-do-user-9694370-0.b.db.ondigitalocean.com",
            user="doadmin",
            password="kd90kihylbplo02n",
            port=25060,
            db="defaultdb"
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("USE defaultdb")


class Notification(Database):
    TABLE_CREATION_SQL = '''CREATE TABLE IF NOT EXISTS notifications (
            id integer NOT NULL AUTO_INCREMENT primary key,
            notification_type integer,
            topic text,
            notification_date date,
            created_at timestamp,
            updated_at timestamp,
            status integer )'''

    INSERT_SQL = '''INSERT INTO notifications (
        notification_type, topic, notification_date, created_at, updated_at, status)
        VALUES (%s, %s, %s, %s, %s, %s)'''

    SELECT_ALL_SQL = '''SELECT * FROM notifications'''
    SELECT_SQL_BY_DATE = '''SELECT * FROM notifications WHERE notification_date=%s'''
    DELETE_SQL = '''DELETE FROM notifications WHERE id = %s'''
    UPDATE_SQL = '''UPDATE notifications SET status=%s, updated_at=%s WHERE id = %s '''
    SELECT_BY_ID_SQL = '''SELECT * FROM notifications WHERE id=%s'''
    SELECT_BY_STATUS_SQL = '''SELECT * FROM notifications WHERE status = 1 and notification_date=%s'''

    def __init__(self):
        super().__init__()

    def create_table(self):
        self.cursor.execute(Notification.TABLE_CREATION_SQL)
        self.connection.commit()

    def update_status(self, notification_id, new_status):
        self.cursor.execute(Notification.UPDATE_SQL,
                            (new_status, datetime.datetime.now(), notification_id))
        self.connection.commit()
        print("status is updated")
        return self.cursor, self.connection

    def delete(self, notification_id):
        self.cursor.execute(Notification.DELETE_SQL, notification_id)

    def add(self, topic, notification_date):
        self.cursor.execute(Notification.INSERT_SQL, (0, topic, notification_date,
                                                      datetime.datetime.now(), datetime.datetime.now(), 1))
        self.connection.commit()

    def get_notifications(self, notification_date=None):
        if notification_date:
            self.cursor.execute(
                Notification.SELECT_SQL_BY_DATE, (notification_date,))
        else:
            self.cursor.execute(Notification.SELECT_ALL_SQL)
        return self.cursor, self.connection

    def get_notification_by_id(self, notification_id):
        self.cursor.execute(Notification.SELECT_BY_ID_SQL, (notification_id,))
        return self.cursor, self.connection

    def get_enabled_notifications(self, notification_date):
        self.cursor.execute(
            Notification.SELECT_BY_STATUS_SQL, (notification_date,))
        return self.cursor, self.connection


class MailAddress(Database):
    TABLE_CREATION_SQL = '''CREATE TABLE IF NOT EXISTS emails (
    id integer NOT NULL AUTO_INCREMENT primary key, mail_address text)'''
    INSERT_SQL = '''INSERT INTO emails (mail_address) VALUES (%s)'''
    GET_ALL_SQL = '''SELECT * FROM emails'''

    def __init__(self):
        super().__init__()

    def create_table(self):
        self.cursor.execute(MailAddress.TABLE_CREATION_SQL)
        self.connection.commit()

    def add(self, mail_address):
        self.cursor.execute(MailAddress.INSERT_SQL, (mail_address,))
        self.connection.commit()

    def get_emails(self):
        self.cursor.execute(MailAddress.GET_ALL_SQL)
        return self.cursor, self.connection


if __name__ == '__main__':
    Notification().add('Сергей Светлаков', '17.05.2021')
    notification = Notification()
    cursor, connection = notification.get_notifications()
