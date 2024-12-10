import unittest
from datetime import date
from GoogleAnalyticsReader import GoogleAnalyticsReader

class GoogleAnalyticsReaderTest(unittest.TestCase):

    def test_getDateRange(self):
        # Given
            
        # When
        dateRange = GoogleAnalyticsReader.getDateRange(dataDir = 'src/testdata/GoogleAnalytics')
        
        # Then
        self.assertEqual(dateRange, (date(2023, 3, 2), date(2023, 9, 29)))
