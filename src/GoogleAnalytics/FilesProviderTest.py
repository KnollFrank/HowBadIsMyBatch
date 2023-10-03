import unittest
from GoogleAnalytics.ResolutionProvider import Resolution
from GoogleAnalytics.FilesProvider import FilesProvider

class FilesProviderTest(unittest.TestCase):

    def test_getFilesHavingCityResolution(self):
        # Given
        filesProvider = FilesProvider(dataDir = 'src/testdata/GoogleAnalytics')
            
        # When
        files = filesProvider.getFilesHavingResolution(Resolution.CITY)
        
        # Then
        self.assertEqual(files, ['src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv'])

    def test_getFilesHavingCountryResolution(self):
        # Given
        filesProvider = FilesProvider(dataDir = 'src/testdata/GoogleAnalytics')
            
        # When
        files = filesProvider.getFilesHavingResolution(Resolution.COUNTRY)
        
        # Then
        self.assertEqual(
            files,
            [
                'src/testdata/GoogleAnalytics/CountryByBatchcode 20230501-20230531.csv',
                'src/testdata/GoogleAnalytics/CountryByBatchcode 20230302-20230430.csv'
            ])
