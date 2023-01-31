import unittest
from pandas.testing import assert_frame_equal
from TableByBatchcodeFilter import TableByBatchcodeFilter
from TestHelper import TestHelper
import pandas as pd

class TableByBatchcodeFilterTest(unittest.TestCase):

    def test_convertHistogramTable2JsonTable_2_VAX_LOT_columns(self):
        # Given
        batchcode = '1808982'
        symptomHistogramByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  ['{"Blood pressure orthostatic abnormal":5,"Chest discomfort":1}'],
                          ['{"Chest discomfort":2}'],
                          ['{"Chills":5}']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [[batchcode,  'EW0175'],
                              ['015M20A',  batchcode],
                              ['015M20A',  'EW0175']]))

        # When
        filteredTable = TableByBatchcodeFilter.filterTableByBatchcode(batchcode, symptomHistogramByBatchcodeTable)

        # Then
        assert_frame_equal(
            filteredTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  ['{"Blood pressure orthostatic abnormal":5,"Chest discomfort":1}'],
                          ['{"Chest discomfort":2}']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [[batchcode,  'EW0175'],
                              ['015M20A',  batchcode]])))

    def test_convertHistogramTable2JsonTable_3_VAX_LOT_columns(self):
        # Given
        batchcode = '1808983'
        symptomHistogramByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  ['{"Blood pressure orthostatic abnormal":5,"Chest discomfort":1}'],
                          ['{"Chest discomfort":2}'],
                          ['{"Chills":5}']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'VAX_LOT3'],
                    tuples = [[batchcode,  'EW0175',   None],
                              ['015M20A',  None,       batchcode],
                              ['015M20A',  'EW0175',   'dummy2']]))

        # When
        filteredTable = TableByBatchcodeFilter.filterTableByBatchcode(batchcode, symptomHistogramByBatchcodeTable)

        # Then
        assert_frame_equal(
            filteredTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  ['{"Blood pressure orthostatic abnormal":5,"Chest discomfort":1}'],
                          ['{"Chest discomfort":2}']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'VAX_LOT3'],
                    tuples = [[batchcode,  'EW0175',   None],
                              ['015M20A',  None,       batchcode]])))
