import unittest
from SmartRegexpFactory import SmartRegexpFactory


class SmartRegexpFactoryTest(unittest.TestCase):

    def test_smartSearch(self):
        def smartSearch(searchTerm, str):
            smartRegexp = SmartRegexpFactory().createSmartRegexp(searchTerm)
            return bool(smartRegexp.match(str))

        self.assertTrue(smartSearch(searchTerm = 'one two three', str = 'one two three'))
        self.assertTrue(smartSearch(searchTerm = 'one two three', str = 'ONE two ThReE'))
        self.assertFalse(smartSearch(searchTerm = 'one two three', str = 'one two'))
        self.assertFalse(smartSearch(searchTerm = 'one two three', str = 'three two'))
        self.assertTrue(smartSearch(searchTerm = 'one two three', str = 'three two one'))
        self.assertTrue(smartSearch(searchTerm = 'one two three', str = 'TESTone twoTEST TESTthreeTEST'))
        self.assertTrue(smartSearch(searchTerm = 'eins zwei drei', str = 'drei, EINS oder zwei?'))
        self.assertFalse(smartSearch(searchTerm = 'eins zwei drei', str = 'drei, ONE oder zwei?'))
        
