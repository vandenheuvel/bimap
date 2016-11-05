"""
Test clearing the bimap.
"""

import unittest
from bimap.bimap import BiMap


class TestClear(unittest.TestCase):
    """
    Test clearing a bimap.
    """

    def test_clear_empty(self):
        """Clear an empty bimap."""
        bimap = BiMap()
        bimap.clear()

        self.assertEqual(0, len(bimap))

    def test_clear_nonempty(self):
        """Clear a nonempty bimap."""
        bimap = BiMap({1: "first", 2: "second"})
        bimap.clear()

        self.assertEqual(0, len(bimap))


if __name__ == '__main__':
    unittest.main()
