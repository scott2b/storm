import unittest

from creepin import na

class TestNA(unittest.TestCase):

    def test_na(self):
        self.assertFalse(na.na())
