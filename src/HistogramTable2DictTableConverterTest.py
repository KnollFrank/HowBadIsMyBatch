import unittest
from pandas.testing import assert_frame_equal
from HistogramTable2DictTableConverter import HistogramTable2DictTableConverter
from TestHelper import TestHelper
import pandas as pd

class HistogramTable2DictTableConverterTest(unittest.TestCase):

    def test_convertHistogramTable2DictTable(self):
        # Given
        histogramTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT', 'COUNTRY'],
                data = [  [5,                          'Germany'],
                          [1,                          'Germany'],
                          [2,                          'Russian Federation']],
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
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT',                     'COUNTRY'],
                data = [  [
                            {
                                "Blood pressure orthostatic abnormal": 5,
                                "Chest discomfort": 1
                            },
                                                                           'Germany'
                          ],
                          [
                            {
                                "Chest discomfort": 2
                            },
                                                                           'Russian Federation'
                          ]],
                index = pd.Index(
                    name =  'VAX_LOT1',
                    data = ['1808982',
                            'EW0175'])))

    def test_convertHistogramTable2DictTable2(self):
        # Given
        histogramTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT', 'COUNTRY'],
                data = [  [5,                          'Germany'],
                          [1,                          'Russian Federation'],
                          [2,                          'Russian Federation']],
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
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT',                     'COUNTRY'],
                data = [  [
                            {
                                "Blood pressure orthostatic abnormal": 5
                            },
                                                                           'Germany'
                          ],
                          [
                            {
                                "Chest discomfort": 1
                            },
                                                                           'Russian Federation'
                          ],
                          [
                            {
                                "Chest discomfort": 2
                            },
                                                                           'Russian Federation'
                          ]],
                index = pd.Index(
                    name =  'VAX_LOT1',
                    data = ['1808982',
                            '1808982',
                            'EW0175'])))

    def test_convertGlobalHistogramTable2DictTable(self):
        # Given
        globalHistogramTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT', 'COUNTRY'],
                data = [  [5,                          'Global'],
                          [1,                          'Global'],
                          [2,                          'Global']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'SYMPTOM'],
                    tuples = [['1808982',  'Blood pressure orthostatic abnormal'],
                              ['1808982',  'Chest discomfort'],
                              ['EW0175',   'Chest discomfort']]))
                
        # When
        dictTable = HistogramTable2DictTableConverter.convertHistogramTable2DictTable(globalHistogramTable)

        # Then
        assert_frame_equal(
            dictTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT',                     'COUNTRY'],
                data = [  [
                            {
                                "Blood pressure orthostatic abnormal": 5,
                                "Chest discomfort": 1
                            },
                                                                           'Global'
                          ],
                          [
                            {
                                "Chest discomfort": 2
                            },
                                                                           'Global'
                          ]],
                index = pd.Index(
                    name =  'VAX_LOT1',
                    data = ['1808982',
                            'EW0175'])))
