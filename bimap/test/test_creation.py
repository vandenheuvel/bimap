"""
Test the creation methods of bimap.
"""

import unittest
from bimap.bimap import BiMap


class TestCreateEmpty(unittest.TestCase):
    """
    Test the constructor.
    """

    def setUp(self):
        self.bimap = BiMap()

    def test_new_map_is_empty(self):
        """Test whether a newly created bimap is empty if not given any arguments."""
        self.assertEqual(dict(), self.bimap.get_key_to_value())
        self.assertEqual(dict(), self.bimap.get_value_to_key())
        self.assertEqual(0, len(self.bimap))


class TestCreateFromDict(unittest.TestCase):
    """
    Test the creation of bimap from another dictionary.
    """

    def test_empty_dict(self):
        """Test creation of bimap from empty dictionary."""
        bimap = BiMap(dict())

        self.assertEqual(0, len(bimap))

        self.assertEqual(dict(), bimap.get_key_to_value())
        self.assertEqual(dict(), bimap.get_value_to_key())

    def test_nonempty_dict(self):
        """Test creation of bimap from nonemtpy dictionary."""
        dictionary = {1: "first", 2: "second"}
        bimap = BiMap(dictionary)

        reverse = dict()
        for key in dictionary:
            reverse[dictionary[key]] = key

        self.assertEqual(2, len(bimap))

        self.assertEqual(dictionary, bimap.get_key_to_value())
        self.assertEqual("first", bimap.get_key(1))

        self.assertEqual(2, bimap.get_value("second"))
        self.assertEqual(reverse, bimap.get_value_to_key())



if __name__ == '__main__':
    unittest.main()
