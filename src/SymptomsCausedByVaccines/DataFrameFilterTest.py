import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.DataFrameFilter import DataFrameFilter

class DataFrameFilterTest(unittest.TestCase):

    def test_withoutZeroRowsAndZeroColumns(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
                columns = ['col1', 'zero column'],
                data = [  [0.6,    0.0],
                          [0.0,    0.0]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ZERO ROW'
                        ]))
        
        # When
        dataFrameWithoutZeroRowsAndZeroColumns = DataFrameFilter.withoutZeroRowsAndZeroColumns(dataFrame)
        
        # Then
        assert_frame_equal(
            dataFrameWithoutZeroRowsAndZeroColumns,
            TestHelper.createDataFrame(
                columns = ['col1'],
                data = [  [0.6]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F'
                        ])))

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
        dataFrameWithoutZeroRows = DataFrameFilter._withoutZeroRows(dataFrame)
        
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
        dataFrameWithoutZeroRows = DataFrameFilter._withoutZeroRows(dataFrame)
        
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

    def test_withoutZeroColumns_noZeroColumn(self):
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
        dataFrameWithoutZeroColumns = DataFrameFilter._withoutZeroColumns(dataFrame)
        
        # Then
        assert_frame_equal(dataFrameWithoutZeroColumns, dataFrame)

    def test_withoutZeroColumns(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
                columns = ['col1', 'zero column'],
                data = [  [0.6,    0.0],
                          [1.2,    0.0]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        '6VAX-G'
                        ]))
        
        # When
        dataFrameWithoutZeroColumns = DataFrameFilter._withoutZeroColumns(dataFrame)
        
        # Then
        assert_frame_equal(
            dataFrameWithoutZeroColumns,
            TestHelper.createDataFrame(
                columns = ['col1'],
                data = [  [0.6],
                          [1.2]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        '6VAX-G'
                        ])))
