import unittest
from SmartSearch import SmartSearch


class SmartSearchTest(unittest.TestCase):

    def test_smartSearch(self):
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('one two three'), True)
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('ONE two ThReE'), True)
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('one two'), False)
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('three two'), False)
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('three two one'), True)
        self.assertEqual(SmartSearch(searchTerm = 'one two three').matches('TESTone twoTEST TESTthreeTEST'), True)
        self.assertEqual(SmartSearch(searchTerm = 'eins zwei drei').matches('drei, EINS oder zwei?'), True)
        self.assertEqual(SmartSearch(searchTerm = 'eins zwei drei').matches('drei, ONE oder zwei?'), False)
