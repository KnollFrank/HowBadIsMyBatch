import unittest
from pandas.testing import assert_frame_equal
from src.DataFrameJoinAndDeduplicate import DataFrameJoinAndDeduplicate
from TestHelper import TestHelper

class DataFrameJoinAndDeduplicateTest(unittest.TestCase):

    def test_mergeListOfDataframesAndDeduplicateByIndex(self):
        # Given
        left = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL'],
            data = [  [1,      0,          0,         1],
                      [0,      1,          0,         1],
                      [0,      0,          1,         0]],
            index = [
                      "0916600",
                      "0916600",
                      "0916601"])
        right = TestHelper.createDataFrame(
            columns = ['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  ['COVID19',  'MODERNA',  '037K20A', '1'],
                      ['COVID19',  'MODERNA',  '037K20B', '1'],
                      ['COVID19',  'MODERNA',  '025L20A', '1']],
            index = [
                      "0916600",
                      "0916600",
                      "0916601"],
            dtypes = {"VAX_DOSE_SERIES": "string"})

        # When
        mergedDataFrame = DataFrameJoinAndDeduplicate.mergeListOfDataframesAndDeduplicateByIndex([(left, right)])
        
        # Then
        mergedDataFrameExpected = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL', 'VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  [0,       0,         1,         0,          'COVID19',  'MODERNA',  '025L20A', '1']],
            index = ["0916601"],
            dtypes = {"VAX_DOSE_SERIES": "string"})
        assert_frame_equal(mergedDataFrame, mergedDataFrameExpected, check_dtype = False)
