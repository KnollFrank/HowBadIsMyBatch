import unittest
from DataFrameNormalizer import DataFrameNormalizer
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import numpy as np

class DataFrameNormalizerTest(unittest.TestCase):

    def test_convertVAX_LOTColumnToUpperCase(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['VAX_LOT'],
            data = [  ['037K20A'],
                      ['025l20A'],
                      ['025L20A']],
            index = [
                "0916600",
                "0916601",
                "1996874"])
            
        # When
        DataFrameNormalizer.convertVAX_LOTColumnToUpperCase(dataFrame)
        
        # Then
        dataFrameExpected = TestHelper.createDataFrame(
            columns = ['VAX_LOT'],
            data = [  ['037K20A'],
                      ['025L20A'],
                      ['025L20A']],
            index = [
                "0916600",
                "0916601",
                "1996874"])
        assert_frame_equal(dataFrame, dataFrameExpected, check_dtype = False)

    def test_removeUnknownBatchCodes(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['VAX_LOT'],
            data = [  ['UNKNOWN'],
                      ['N/A Unknown'],
                      [np.nan],
                      ['UNKNOWN TO ME'],
                      ['030L20B']],
            index = [
                "1048786",
                "1048786",
                "123",
                "4711",
                "0815"])
            
        # When
        DataFrameNormalizer.removeUnknownBatchCodes(dataFrame)
        
        # Then
        dataFrameExpected = TestHelper.createDataFrame(
            columns = ['VAX_LOT'],
            data = [  [np.nan],
                      ['030L20B']],
            index = [
                "123",
                "0815"])
        assert_frame_equal(dataFrame, dataFrameExpected, check_dtype = False)