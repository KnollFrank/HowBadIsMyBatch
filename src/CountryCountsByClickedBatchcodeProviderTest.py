import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from CountryCountsByClickedBatchcodeProvider import CountryCountsByClickedBatchcodeProvider

class CountryCountsByClickedBatchcodeProviderTest(unittest.TestCase):

    def test_mergeCountryCountsByBatchcodeTables(self):
        # Given
            
        # When
        countryCountsByClickedBatchcodeTable = CountryCountsByClickedBatchcodeProvider.getCountryCountsByClickedBatchcode('src/testdata/GoogleAnalytics/CountryByBatchcode 20230302-20230430.csv')
        
        # Then
        assert_frame_equal(
            countryCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT'],
                data = [  [1],
                          [10],
                          [5]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY'],
                            tuples = [['#012M20A', 'United States'],
                                      ['#EN6203',  'United States'],
                                      ['000006A',  'Japan']])))
