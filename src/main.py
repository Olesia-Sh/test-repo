#!/usr/bin/python3
from conrun import Mysql

class Shop(Mysql):


    def create_shop(self):
        query = "CREATE DATABASE IF NOT EXISTS shop3"
        self.run_query(query)
        query = "USE shop3"
        self.run_query(query)
        query = "CREATE TABLE shop3 (id INT AUTO_INCREMENT PRIMARY KEY, item VARCHAR(255), price INT)"
        self.run_query(query)
        print("Shop3 table created.")

    def add_item(self, item, price):
        query = f"INSERT INTO shop3 (item, price) VALUES ('{item}', {price})"
        self.run_query(query)
        print(f"Item '{item}' added to the shop3.")

    def delete_item(self, item):
        query = f"DELETE FROM shop3 WHERE item = '{item}'"
        self.run_query(query)
        print(f"Item '{item}' deleted from the shop3.")

    def delete_shop(self):
        query = "DROP TABLE shop3"
        self.run_query(query)
        print("Shop3 table deleted.")

host="192.168.88.15"
user="seller"
password="abc123"


myshop = Shop(host, user, password)
myshop.connect_db()
myshop.create_shop()
myshop.add_item("Tomato", 5)
myshop.add_item("Lemon", 3)
myshop.delete_item("Lemon")
myshop.delete_shop()
