import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountryColumnAdder import CountryColumnAdder


class CountryColumnAdderTest(unittest.TestCase):
    
    def test_addCountryColumn(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['SPLTTYPE'],
            data = [  ['GBPFIZER INC2020486806'],
                      ['FRMODERNATX, INC.MOD20224'],
                      ['dummy']],
            index = [
                "4711",
                "0815",
                "123"])
        
        # When
        dataFrameWithCountryColumn = CountryColumnAdder.addCountryColumn(dataFrame)

        # Then
        assert_frame_equal(
            dataFrameWithCountryColumn,
            TestHelper.createDataFrame(
            columns = ['SPLTTYPE',                  'COUNTRY'],
            data = [  ['GBPFIZER INC2020486806',    'United Kingdom'],
                      ['FRMODERNATX, INC.MOD20224', 'France'],
                      ['dummy',                     'Unknown Country']],
            index = [
                "4711",
                "0815",
                "123"],
            dtypes = {'COUNTRY': 'string'}))
