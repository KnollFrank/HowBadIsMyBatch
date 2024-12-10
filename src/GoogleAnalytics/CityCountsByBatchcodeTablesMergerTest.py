import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from datetime import date
from GoogleAnalytics.CityCountsByBatchcodeTablesMerger import CityCountsByBatchcodeTablesMerger

class CityCountsByBatchcodeTablesMergerTest(unittest.TestCase):

    def test_getCityCountsByClickedBatchcode(self):
        # Given

        # When
        cityCountsByClickedBatchcodeTable = CityCountsByBatchcodeTablesMerger.getCityCountsByClickedBatchcode('src/testdata/GoogleAnalytics')
        
        # Then
        assert_frame_equal(
            cityCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['CITY_COUNT_BY_VAX_LOT'],
                data = [  [100 + 200],
                          [10 + 20],
                          [20 + 40 + 400]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION',     'CITY'],
                            tuples = [['#003B21A', 'United States', 'California', 'Roseville'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg']])))

    def test_getCityCountsByClickedBatchcode_includeDateRange(self):
        # Given

        # When
        cityCountsByClickedBatchcodeTable = CityCountsByBatchcodeTablesMerger.getCityCountsByClickedBatchcode('src/testdata/GoogleAnalytics', includeDateRange = True)
        
        # Then
        assert_frame_equal(
            cityCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['CITY_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [200],
                          [10],
                          [20],
                          [20],
                          [40 + 400]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION',     'CITY',       'START_DATE',      'END_DATE'],
                            tuples = [['#003B21A', 'United States', 'California', 'Roseville',  date(2023, 7, 30), date(2023, 9, 29)],
                                      ['#003B21A', 'United States', 'California', 'Roseville',  date(2023, 9, 29), date(2023, 9, 30)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen', date(2023, 7, 30), date(2023, 9, 29)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen', date(2023, 9, 29), date(2023, 9, 30)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg',  date(2023, 7, 30), date(2023, 9, 29)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg',  date(2023, 9, 29), date(2023, 9, 30)]])))
