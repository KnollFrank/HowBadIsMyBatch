import unittest
from GoogleAnalytics.ResolutionProvider import Resolution, ResolutionProvider


class ResolutionProviderTest(unittest.TestCase):

    def test_getResolution_COUNTRY(self):
        # Given

        # When
        resolution = ResolutionProvider.getResolution('src/testdata/GoogleAnalytics/CountryByBatchcode 20230302-20230430.csv')

        # Then
        self.assertEqual(resolution, Resolution.COUNTRY)

    def test_getResolution_CITY(self):
        # Given

        # When
        resolution = ResolutionProvider.getResolution('src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv')

        # Then
        self.assertEqual(resolution, Resolution.CITY)
