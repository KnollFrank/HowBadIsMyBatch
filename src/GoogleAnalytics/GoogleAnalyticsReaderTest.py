import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from datetime import date
from GoogleAnalytics.GoogleAnalyticsReader import GoogleAnalyticsReader

class GoogleAnalyticsReaderTest(unittest.TestCase):

    def test_read_csv(self):
        # Given
        file = 'src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv'

        # When
        table = GoogleAnalyticsReader.read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Region': 'REGION',
                'City': 'CITY',
                'Event count': 'CITY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY', 'REGION', 'CITY'])
        
        # Then
        assert_frame_equal(
            table,
            TestHelper.createDataFrame(
                columns = ['CITY_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [10],
                          [20]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION',     'CITY'],
                            tuples = [['#003B21A', 'United States', 'California', 'Roseville'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen'],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg',]])))

    def test_read_csv_includeDateRange(self):
        # Given
        file = 'src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv'

        # When
        table = GoogleAnalyticsReader.read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Region': 'REGION',
                'City': 'CITY',
                'Event count': 'CITY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY', 'REGION', 'CITY'],
            dateRangeIndexColumns = {
                    'startDate' : 'START_DATE',
                    'endDate': 'END_DATE'
                })
        
        # Then
        assert_frame_equal(
            table,
            TestHelper.createDataFrame(
                columns = ['CITY_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [10],
                          [20]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION',     'CITY',       'START_DATE',      'END_DATE'],
                            tuples = [['#003B21A', 'United States', 'California', 'Roseville',  date(2023, 7, 30), date(2023, 9, 29)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nordlingen', date(2023, 7, 30), date(2023, 9, 29)],
                                      ['000086A',  'Germany',       'Bavaria',    'Nuremberg',  date(2023, 7, 30), date(2023, 9, 29)]])))
