import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountryColumnsMerger import CountryColumnsMerger


class CountryColumnsMergerTest(unittest.TestCase):
    
    def test_mergeCountryColumnOfSrcIntoDst(self):
        # Given
        src_val = 'Germany'
        dst_val = None
        dst = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          ['France'],
                          [dst_val]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'})
        
        src = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          [src_val]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '123']),
                dtypes = {'COUNTRY': 'string'})

        # When
        merged = CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src = src, dst = dst)

        # Then
        assert_frame_equal(
            merged,
            TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  ['United Kingdom'],
                          ['France'],
                          [src_val]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'}))

    def test_shouldNotMergeCountryColumnOfSrcIntoDst_non_unique(self):
        self._mergeCountryColumnOfSrcIntoDst(val_dst = 'United Kingdom', val_src = 'Germany')

    def test_shouldNotMergeCountryColumnOfSrcIntoDst3(self):
        self._mergeCountryColumnOfSrcIntoDst(val_dst = None, val_src = None)

    def _mergeCountryColumnOfSrcIntoDst(self, val_dst, val_src):
        # Given
        dst = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  [val_dst]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711']),
                dtypes = {'COUNTRY': 'string'})
        
        src = TestHelper.createDataFrame(
                columns = ['COUNTRY'],
                data = [  [val_src]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711']),
                dtypes = {'COUNTRY': 'string'})

        # When && Then
        with self.assertRaises(Exception):
            CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src = src, dst = dst)
