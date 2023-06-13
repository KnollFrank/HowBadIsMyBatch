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
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [dst_val,          'test3']],
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
        merged = CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src, dst)

        # Then
        assert_frame_equal(
            merged,
            TestHelper.createDataFrame(
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [src_val,          'test3']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'}),
                check_like = True)

    def test_mergeCountryColumnOfSrcIntoDst_non_unique_index(self):
        # Given
        src_val = 'Germany'
        dst_val = None
        dst = TestHelper.createDataFrame(
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [dst_val,          'test3']],
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
                          [src_val],
                          [src_val]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '123',
                            '123']),
                dtypes = {'COUNTRY': 'string'})

        # When
        merged = CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src, dst)

        # Then
        assert_frame_equal(
            merged,
            TestHelper.createDataFrame(
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [src_val,          'test3']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'}),
                check_like = True)

    def test_mergeCountryColumnOfSrcIntoDst_None_None(self):
        # Given
        src_val = None
        dst_val = None
        dst = TestHelper.createDataFrame(
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [dst_val,          'test3']],
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
        merged = CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src, dst)

        # Then
        assert_frame_equal(
            merged,
            TestHelper.createDataFrame(
                columns = ['COUNTRY',        'TestColumn'],
                data = [  ['United Kingdom', 'test1'],
                          ['France',         'test2'],
                          [src_val,          'test3']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            '4711',
                            '0815',
                            '123']),
                dtypes = {'COUNTRY': 'string'}),
                check_like = True)

    def test_shouldNotMergeCountryColumnOfSrcIntoDst_non_unique(self):
        # Given
        val_dst = 'United Kingdom'
        val_src = 'Germany'
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
            CountryColumnsMerger.mergeCountryColumnOfSrcIntoDst(src, dst)
