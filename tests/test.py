#!/usr/bin/python3
import unittest
from main import Shop


class TestMysql(unittest.TestCase):
  def setUp(self):
      self.mysqlclass = Shop("192.168.88.15", "seller", "abc123", "shop3") #створює екземпляр нашого класу
      print("Connected!!!!!!!!!!")
  def test_create_item(self):
      self.mysqlclass.create_shop()
      res = self.mysqlclass.add_item("Tomato", 5)
      print(f"Res: {res}")
      expected = [(1, 'Tomato', 5)]
      self.assertEqual(expected, res)

  def drop_table(self):
      self.mysqlclass.delete_shop()





if __name__ == "__main__":
    print("Start unit test!!!!!!!!!")
    unittest.main()
