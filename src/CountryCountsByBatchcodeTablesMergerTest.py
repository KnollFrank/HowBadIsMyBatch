import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from CountryCountsByBatchcodeTablesMerger import CountryCountsByBatchcodeTablesMerger

class CountryCountsByBatchcodeTablesMergerTest(unittest.TestCase):

    def test_mergeCountryCountsByBatchcodeTables(self):
        # Given
        countryCountsByBatchcodeTable1 = TestHelper.createDataFrame(
            columns = ['COUNTRY_COUNT_BY_VAX_LOT'],
            data = [  [10],
                      [15]],
            index = pd.MultiIndex.from_tuples(
                        names =   ['VAX_LOT', 'COUNTRY'],
                        tuples = [['12345',   'Germany'],
                                  ['AAA',     'United States']]))
        countryCountsByBatchcodeTable2 = TestHelper.createDataFrame(
            columns = ['COUNTRY_COUNT_BY_VAX_LOT'],
            data = [  [20]],
            index = pd.MultiIndex.from_tuples(
                        names =   ['VAX_LOT', 'COUNTRY'],
                        tuples = [['12345',   'Germany']]))
            
        # When
        mergedCountryCountsByBatchcodeTables = CountryCountsByBatchcodeTablesMerger.mergeCountryCountsByBatchcodeTables(
            [
                countryCountsByBatchcodeTable1,
                countryCountsByBatchcodeTable2
            ])
        
        # Then
        assert_frame_equal(
            mergedCountryCountsByBatchcodeTables,
            TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT'],
                data = [  [10 + 20],
                          [15]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT', 'COUNTRY'],
                            tuples = [['12345',   'Germany'],
                                      ['AAA',     'United States']])))

def _getCountryCountsByClickedBatchcode():
    exploration = pd.read_csv('src/data/Country By Clicked Batchcode 20230302-20230430.csv', index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
    exploration.index.name = 'VAX_LOT'
    exploration.rename(
        columns =
        {
            'Country': 'COUNTRY',
            'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
        },
        inplace = True)
    exploration.set_index('COUNTRY',append = True, inplace = True)
    return exploration
