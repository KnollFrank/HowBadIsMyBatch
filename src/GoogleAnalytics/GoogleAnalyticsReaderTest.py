import unittest
from GoogleAnalytics.ResolutionProvider import Resolution
from GoogleAnalytics.GoogleAnalyticsReader import GoogleAnalyticsReader

class GoogleAnalyticsReaderTest(unittest.TestCase):

    def test_getFilesHavingCityResolution(self):
        # Given
        googleAnalyticsReader = GoogleAnalyticsReader(dataDir = 'src/testdata/GoogleAnalytics')
            
        # When
        files = googleAnalyticsReader.getFilesHavingResolution(Resolution.CITY)
        
        # Then
        self.assertEqual(files, ['src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv'])

    def test_getFilesHavingCountryResolution(self):
        # Given
        googleAnalyticsReader = GoogleAnalyticsReader(dataDir = 'src/testdata/GoogleAnalytics')
            
        # When
        files = googleAnalyticsReader.getFilesHavingResolution(Resolution.COUNTRY)
        
        # Then
        self.assertEqual(
            files,
            [
                'src/testdata/GoogleAnalytics/CountryByBatchcode 20230501-20230531.csv',
                'src/testdata/GoogleAnalytics/CountryByBatchcode 20230302-20230430.csv'
            ])
