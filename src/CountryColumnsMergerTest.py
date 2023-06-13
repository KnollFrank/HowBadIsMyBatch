import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountryColumnsMerger import CountryColumnsMerger


class CountryColumnsMergerTest(unittest.TestCase):
    
    def test_mergeCountryColumns(self):
        # Given
        unknown = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          ['France'],
                          [None]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'})
        
        known = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          ['Germany']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '123']),
                dtypes = {'COUNTRY': 'string'})

        # When
        merged = CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src = known, dst = unknown)

        # Then
        assert_frame_equal(
            merged,
            TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          ['France'],
                          ['Germany']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'}))
