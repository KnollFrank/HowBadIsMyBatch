import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from CountryCountsByClickedBatchcodeProvider import CountryCountsByClickedBatchcodeProvider

class CountryCountsByClickedBatchcodeProviderTest(unittest.TestCase):

    def test_getCountryCountsByClickedBatchcode_fromCountryResolution(self):
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

    def test_getCityCountsByClickedBatchcode(self):
        # Given

        # When
        cityCountsByClickedBatchcodeTable = CountryCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode('src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv')
        
        # Then
        assert_frame_equal(
            cityCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['CITY_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [10],
                          [20]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION',     'CITY'],
                            tuples = [['#003B21A', 'United States', 'California', 'Roseville'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg']])))

    def test_getCountryCountsByClickedBatchcode_fromCityResolution(self):
        # Given

        # When
        countryCountsByClickedBatchcodeTable = CountryCountsByClickedBatchcodeProvider.getCountryCountsByClickedBatchcode('src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv')
        
        # Then
        assert_frame_equal(
            countryCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [10 + 20]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY'],
                            tuples = [['#003B21A', 'United States'],
                                      ['000086A',  'Germany']])))
