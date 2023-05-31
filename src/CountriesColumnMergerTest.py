import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from src.CountriesColumnMerger import CountriesColumnMerger

class CountriesColumnMergerTest(unittest.TestCase):

    def test_mergeCountriesColumnOfSrcIntoCountriesColumnOfDst(self):
        # Given
        dst = TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [[]],
                          [['France', 'United Kingdom']],
                          [['France']]],
                index = pd.Index(
                    [
                        '016M20A',
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT'))

        src = TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [['Germany']],
                          [['DummyCountry']]],
                index = pd.Index(
                    [
                        '030L20B',
                        'dummyVaxLot'
                    ],
                    name = 'VAX_LOT'))
        
        # When
        CountriesColumnMerger.mergeCountriesColumnOfSrcIntoCountriesColumnOfDst(dst = dst, src = src)

        # Then
        assert_frame_equal(
            dst,
            TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [[]],
                          [['France', 'Germany', 'United Kingdom']],
                          [['France']]],
                index = pd.Index(
                    [
                        '016M20A',
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
