import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from CountriesColumnMerger import CountriesColumnMerger

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

    def test_mergeCountriesColumnOfSrcsIntoCountriesColumnOfDst(self):
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

        src1 = TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [['Germany1']]],
                index = pd.Index(
                    [
                        '030L20B'
                    ],
                    name = 'VAX_LOT'))

        src2 = TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [['Germany2']]],
                index = pd.Index(
                    [
                        '030L20B'
                    ],
                    name = 'VAX_LOT'))

        # When
        CountriesColumnMerger.mergeCountriesColumnOfSrcsIntoCountriesColumnOfDst(dst = dst, srcs = [src1, src2])

        # Then
        assert_frame_equal(
            dst,
            TestHelper.createDataFrame(
                columns = ['Countries'],
                data = [  [[]],
                          [['France', 'Germany1', 'Germany2', 'United Kingdom']],
                          [['France']]],
                index = pd.Index(
                    [
                        '016M20A',
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
