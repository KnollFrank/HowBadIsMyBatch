import unittest
from datetime import date
from GoogleAnalyticsReader import GoogleAnalyticsReader

class GoogleAnalyticsReaderTest(unittest.TestCase):

    def test_getDateRange(self):
        # Given
        googleAnalyticsReader = GoogleAnalyticsReader(dataDir = 'src/testdata/GoogleAnalytics')
            
        # When
        dateRange = googleAnalyticsReader.getDateRange()
        
        # Then
        self.assertEqual(dateRange, (date(2023, 3, 2), date(2023, 9, 29)))
