import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from TablesHelper import TablesHelper

class TablesHelperTest(unittest.TestCase):

    def test_concatTables_groupByIndex_sum(self):
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
        mergedCountryCountsByBatchcodeTables = TablesHelper.concatTables_groupByIndex_sum(
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
