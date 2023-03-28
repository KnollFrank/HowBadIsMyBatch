import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountriesColumnAdder import CountriesColumnAdder

class CountriesColumnAdderTest(unittest.TestCase):
    
    def test_addCountriesColumn(self):
        # Given
        countriesByBatchcodeTable = TestHelper.createDataFrame(
            columns = ['United States', 'Germany', 'Italy'],
            data = [  [20,              0,         3]],
            index = pd.Index(
                    name = 'Batchcode',
                    data = ['FE6208']))
        columnName = 'Countries guessed'

        # When
        countriesByBatchcodeTableWithCountriesColumn = CountriesColumnAdder().addCountriesColumn(countriesByBatchcodeTable, columnName)

        # Then
        assert_frame_equal(
            countriesByBatchcodeTableWithCountriesColumn,
            TestHelper.createDataFrame(
                columns = ['United States', 'Germany', 'Italy', columnName],
                data = [  [20,              0,         3,       {'United States', 'Italy'}]],
                index = pd.Index(
                        name = 'Batchcode',
                        data = ['FE6208'])))
        