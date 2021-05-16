from ..store.inventory import *

import unittest

class TestFind(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory(
            Item('item1', 2),
            Item('item2', 0),
            Item('item3', -1),
            Item('item4', 4000)
            )
    
    def test_find_first_item(self):
        correct = Item('item1', 2)
        actual = self.inv.find('item1')
        self.assertEqual(correct.item_type, actual.item_type)
        self.assertEqual(correct.quantity, actual.quantity)
    
    def test_find_last_item(self):
        correct = Item('item4', 4000)
        actual = self.inv.find('item4')
        self.assertEqual(correct.item_type, actual.item_type)
        self.assertEqual(correct.quantity, actual.quantity)

    def test_find_missing_item(self):
        with self.assertRaises(InvalidItemType):
            self.inv.find('invalid item')


class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory(
            Item('item1', 2),
            Item('item2', 0),
            Item('item3', -1),
            Item('item4', 4000)
            )
    
    def test_valid_purchase(self):
        quantity = self.inv.items[0].quantity
        ret_value = self.inv.purchase('item1')
        # proper return value
        self.assertEqual(ret_value, quantity - 1)
        # quantity properly decremented
        self.assertEqual(self.inv.items[0].quantity, ret_value)

    def test_multiple_purchases(self):
        start_quantity = self.inv.items[3].quantity
        for i in range(2000):
            self.inv.purchase('item4')
        self.assertEqual(start_quantity - 2000, self.inv.items[3].quantity)

    def test_invalid_item_purchase(self):
        with self.assertRaises(InvalidItemType):
            self.inv.purchase('invalid item')
    
    def test_out_of_stock_purchase(self):
        with self.assertRaises(OutOfStock):
            self.inv.purchase('item2')
        with self.assertRaises(OutOfStock):
            self.inv.purchase('item3')