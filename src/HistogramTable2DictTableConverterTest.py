import unittest
from pandas.testing import assert_frame_equal
from HistogramTable2DictTableConverter import HistogramTable2DictTableConverter
from TestHelper import TestHelper
import pandas as pd

class HistogramTable2DictTableConverterTest(unittest.TestCase):

    def test_convertHistogramTable2DictTable(self):
        # Given
        histogramTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [5],
                          [1],
                          [2]],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'SYMPTOM'],
                    tuples = [['1808982',  'Blood pressure orthostatic abnormal'],
                              ['1808982',  'Chest discomfort'],
                              ['EW0175',   'Chest discomfort']]))
                
        # When
        dictTable = HistogramTable2DictTableConverter.convertHistogramTable2DictTable(histogramTable)

        # Then
        assert_frame_equal(
            dictTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [
                            {
                                "Blood pressure orthostatic abnormal": 5,
                                "Chest discomfort": 1
                            }
                          ],
                          [
                            {
                                "Chest discomfort": 2
                            }
                          ]],
                index = pd.Index(
                    name =  'VAX_LOT1',
                    data = ['1808982',
                            'EW0175'])))
