import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountriesByBatchcodeProvider import filterByBatchcodes

class CountriesByBatchcodeProviderTest(unittest.TestCase):
    
    def test_filterByBatchcodes(self):
        # Given
        countryCountsByBatchcode = TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT Clicked', 'COUNTRY_COUNT_BY_VAX_LOT Before Deletion'],
                data = [  [10,                                 20],
                          [90,                                 95],
                          [15,                                 30],
                          [70,                                 80]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',   'COUNTRY'],
                            tuples = [('!D0181',    'Germany'),
                                      ('# 009C01A', 'United States'),
                                      ('!D0181',    'Hungary'),
                                      ('# 009C01A', 'Germany')]))

        # When
        countryCountsByBatchcodeFiltered = filterByBatchcodes(countryCountsByBatchcode, ['!D0181'])

        # Then
        assert_frame_equal(
            countryCountsByBatchcodeFiltered,
            TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT Clicked', 'COUNTRY_COUNT_BY_VAX_LOT Before Deletion'],
                data = [  [10,                                 20],
                          [15,                                 30]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',   'COUNTRY'],
                            tuples = [('!D0181',    'Germany'),
                                      ('!D0181',    'Hungary')])))
        