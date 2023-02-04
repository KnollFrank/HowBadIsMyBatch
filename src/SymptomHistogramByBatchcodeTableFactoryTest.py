import unittest
from pandas.testing import assert_frame_equal
from SymptomHistogramByBatchcodeTableFactory import SymptomHistogramByBatchcodeTableFactory
from TestHelper import TestHelper
import pandas as pd

class SymptomHistogramByBatchcodeTableFactoryTest(unittest.TestCase):

    def test_createSymptomHistogramByBatchcodeTable(self):
        # Given
        symptomByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM'],
                data = [  ['Blood pressure orthostatic abnormal'],
                          ['Blood pressure orthostatic abnormal'],
                          ['Blood pressure orthostatic abnormal']],
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
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [1],
                          [2]],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'SYMPTOM'],
                    tuples = [['1808982',  'Blood pressure orthostatic abnormal'],
                              ['EW0175',   'Blood pressure orthostatic abnormal']])))

    def test_createSymptomHistogramByBatchcodeTable_two_VAX_LOTs_Index(self):
        # Given
        symptomByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM'],
                data = [  ['Blood pressure orthostatic abnormal'],
                          ['Blood pressure orthostatic abnormal'],
                          ['Headache']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982',  'EW0175']] * 3))
                        
        # When
        symptomHistogramByBatchcodeTable = SymptomHistogramByBatchcodeTableFactory.createSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable)

        # Then
        assert_frame_equal(
            symptomHistogramByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [2],
                          [1]],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'SYMPTOM'],
                    tuples = [['1808982',  'EW0175',   'Blood pressure orthostatic abnormal'],
                              ['1808982',  'EW0175',   'Headache']])))