import unittest
import pandas as pd
from CountriesMerger import CountriesMerger
from pandas.testing import assert_series_equal


class CountriesMergerTest(unittest.TestCase):

    def test_mergeSrcIntoDst(self):
        # Given
        dstCountries = pd.Series({'NO72A': {'CountryA-1'}, 'EW096': {'CountryA-2'}}, name='dstCountries')
        srcCountries = pd.Series({'NO72A': 'CountryB-1',   'FS192': 'CountryB-2'}, name='srcCountries')

        # When
        mergedCountries = CountriesMerger.mergeSrcIntoDst(src = srcCountries, dst = dstCountries)

        # Then
        assert_series_equal(
            mergedCountries,
            pd.Series(
                {
                    'NO72A': ['CountryA-1', 'CountryB-1'],
                    'EW096': ['CountryA-2']
                }))
