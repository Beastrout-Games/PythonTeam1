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
