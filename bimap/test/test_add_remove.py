"""
Test the adding and removing of items.
"""

import unittest
from bimap.bimap import BiMap


class TestAddSingleItem(unittest.TestCase):
    """
    Test adding a single item.
    """

    def test_add_by_key_to_empty(self):
        """Test adding a single item to empty bimap by key."""
        bimap = BiMap()
        bimap.add_key(1, "first")

        self.assertEqual({1: "first"}, bimap.get_key_to_value())
        self.assertEqual(1, len(bimap))
        self.assertEqual("first", bimap.get_key(1))
        self.assertEqual(1, bimap.get_value("first"))

    def test_add_by_value_to_empty(self):
        """Test adding a single item to empty bimap by value."""
        bimap = BiMap()
        bimap.add_value("first", 1)

        self.assertEqual({1: "first"}, bimap.get_key_to_value())
        self.assertEqual(1, len(bimap))
        self.assertEqual(1, bimap.get_value("first"))
        self.assertEqual("first", bimap.get_key(1))

    def test_add_to_nonempty(self):
        """Test adding a single item to nonempty bimap."""
        bimap = BiMap({1: "first", 2: "second"})
        bimap.add_key(3, "third")
        bimap.add_value("fourth", 4)

        self.assertEqual(4, len(bimap))
        self.assertEqual("second", bimap.get_key(2))
        self.assertEqual("fourth", bimap.get_key(4))
        self.assertEqual(3, bimap.get_value("third"))


class TestAddMultipleItems(unittest.TestCase):
    """
    Test adding multiple items at once.
    """

    def test_add_by_key_to_empty(self):
        """Test adding multiple items to an empty bimap by key."""
        bimap = BiMap()
        bimap.update_by_key({1: "first", 2: "second"})

        self.assertEqual(2, len(bimap))
        self.assertEqual("first", bimap.get_key(1))
        self.assertEqual(2, bimap.get_value("second"))

    def test_add_by_value_to_empty(self):
        """Test adding multiple items to an empty bimap by value."""
        bimap = BiMap()
        bimap.update_by_value({"first": 1, "second": 2})

        self.assertEqual(2, len(bimap))
        self.assertEqual("first", bimap.get_key(1))
        self.assertEqual(2, bimap.get_value("second"))

    def test_add_to_nonempty(self):
        """Test adding multiple items to nonempty bimap."""
        bimap = BiMap({1: "first", 2: "second"})
        bimap.update_by_value({"third": 3, "fourth": 4})
        bimap.update_by_key({2: "secondNew", 3: "thirdNew"})

        self.assertEqual(4, len(bimap))
        self.assertEqual("first", bimap.get_key(1))
        self.assertEqual("secondNew", bimap.get_key(2))
        self.assertEqual(3, bimap.get_value("thirdNew"))
        self.assertEqual(4, bimap.get_value("fourth"))



if __name__ == '__main__':
    unittest.main()
