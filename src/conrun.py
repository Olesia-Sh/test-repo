#!/usr/bin/python3
import mysql.connector
import time

class Mysql():
    def __init__(self, host, user, password):

        max_retries = 30
        retries = 0


        while True:

            try:

               self.conn = mysql.connector.connect(
                   host=host,
                   user=user,
                   password=password

               )

               print("MySql is ready")
               break
            except mysql.connector.Error as err:
               print(f"Waiting for MySql....({err})")
               time.sleep(1)
               retries += 1

               if retries >= max_retries:
                    print("Unable to connect to MySql")
                    exit(1)
         

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
