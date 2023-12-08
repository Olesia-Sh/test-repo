#!/usr/bin/python3
import mysql.connector

class Mysql():
    def __init__(self, host, user, password):
            self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password

        )
            self.cursor = self.conn.cursor()
    def connect_db(self):
        self.conn.connect()


    def run_query(self, text):
        self.cursor.execute(text)
        try:
            self.conn.commit()
        except Exception:
             pass
        return self.cursor.fetchall()
