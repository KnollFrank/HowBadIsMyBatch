import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.DataFrameFilter import DataFrameFilter

class DataFrameFilterTest(unittest.TestCase):

    def test_withoutZeroRows_noZeroRow(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
                columns = ['col1', 'col2'],
                data = [  [0.6,    1.5],
                          [0.3,    3.0]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ADEN'
                        ]))
        
        # When
        dataFrameWithoutZeroRows = DataFrameFilter.withoutZeroRows(dataFrame)
        
        # Then
        assert_frame_equal(dataFrameWithoutZeroRows, dataFrame)

    def test_withoutZeroRows(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
                columns = ['col1', 'col2'],
                data = [  [0.6,    1.5],
                          [0.0,    0.0]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ZERO ROW'
                        ]))
        
        # When
        dataFrameWithoutZeroRows = DataFrameFilter.withoutZeroRows(dataFrame)
        
        # Then
        assert_frame_equal(
            dataFrameWithoutZeroRows,
            TestHelper.createDataFrame(
                columns = ['col1', 'col2'],
                data = [  [0.6,    1.5]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F'
                        ])))
