#!/usr/bin/python3
import unittest
from main import Shop


class TestMysql(unittest.TestCase):
  def setUp(self):
      self.mysqlclass = Shop("mysql", "root", "abc123")
      print("Connected!!!!!!!!!!")
  def test_create_item(self):
      self.mysqlclass.create_shop()
      self.mysqlclass.add_item("Tomato", 5)
      query = f"SELECT * FROM shop6"
      res = self.mysqlclass.run_query(query)
      print(f"Res: {res}")
      expected = [(1, 'Tomato', 5)]
      self.mysqlclass.delete_shop()
      self.assertEqual(expected, res)






  #def drop_table(self):
   #   self.mysqlclass.delete_shop()





if __name__ == "__main__":
    print("Start unit test!!!!!!!!!")
    unittest.main()
