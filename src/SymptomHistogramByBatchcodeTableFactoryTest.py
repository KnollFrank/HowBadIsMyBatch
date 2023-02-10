import unittest
from pandas.testing import assert_frame_equal
from SymptomHistogramByBatchcodeTableFactory import SymptomHistogramByBatchcodeTableFactory
from TestHelper import TestHelper
import pandas as pd

class SymptomHistogramByBatchcodeTableFactoryTest(unittest.TestCase):

    def test_createSymptomHistogramByBatchcodeTable(self):
        # Given
        symptomByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM',                             'COUNTRY'],
                data = [  ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Germany']],
                index = pd.Index(
                    name = 'VAX_LOT1',
                    data = ['EW0175',
                            'EW0175',
                            '1808982']))
                
        # When
        symptomHistogramByBatchcodeTable = SymptomHistogramByBatchcodeTableFactory.createSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable)

        # Then
        assert_frame_equal(
            symptomHistogramByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT', 'COUNTRY'],
                data = [  [1,                          'Germany'],
                          [2,                          'Germany']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'SYMPTOM'],
                    tuples = [['1808982',  'Blood pressure orthostatic abnormal'],
                              ['EW0175',   'Blood pressure orthostatic abnormal']])))

    def test_createSymptomHistogramByBatchcodeTable_two_VAX_LOTs_Index(self):
        # Given
        symptomByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM',                             'COUNTRY'],
                data = [  ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Russian Federation'],
                          ['Headache',                            'Germany']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982',  'EW0175']] * 4))
                        
        # When
        symptomHistogramByBatchcodeTable = SymptomHistogramByBatchcodeTableFactory.createSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable)

        # Then
        assert_frame_equal(
            symptomHistogramByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT', 'COUNTRY'],
                data = [  [2,                          'Germany'],
                          [1,                          'Germany'],
                          [1,                          'Russian Federation']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'SYMPTOM'],
                    tuples = [['1808982',  'EW0175',   'Blood pressure orthostatic abnormal'],
                              ['1808982',  'EW0175',   'Headache'],
                              ['1808982',  'EW0175',   'Blood pressure orthostatic abnormal']])))

    def test_createGlobalSymptomHistogramByBatchcodeTable(self):
        # Given
        symptomByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM',                             'COUNTRY'],
                data = [  ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Germany'],
                          ['Blood pressure orthostatic abnormal', 'Russian Federation'],
                          ['Headache',                            'Germany']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982',  'EW0175']] * 4))
                        
        # When
        globalSymptomHistogramByBatchcodeTable = SymptomHistogramByBatchcodeTableFactory.createGlobalSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable)

        # Then
        assert_frame_equal(
            globalSymptomHistogramByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [3],
                          [1]],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'SYMPTOM'],
                    tuples = [['1808982',  'EW0175',   'Blood pressure orthostatic abnormal'],
                              ['1808982',  'EW0175',   'Headache']])))
