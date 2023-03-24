import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CompletedBatchcodeColumnAdder import CompletedBatchcodeColumnAdder
from BatchcodeCompletion import BatchcodeCompletion

class CompletedBatchcodeColumnAdderTest(unittest.TestCase):
    
    def test_addCompletedBatchcodeColumn(self):
        # Given
        def completeBatchcode(partialBatchcode):
            if partialBatchcode == '30L20B':
                return '30L20B_COMPLETION'

        tableByPartialBatchcode = TestHelper.createDataFrame(
            columns = pd.MultiIndex.from_tuples(
                        names =   ['Country',        'Region'],
                        tuples = [['United Kingdom', 'England']]),
            data = [              [4711]],
            index = pd.Index(
                    name = 'Batchcode Search Term',
                    data = ['30L20B']))
        completedBatchcodeColumnAdder = CompletedBatchcodeColumnAdder(completeBatchcode)

        # When
        dataFrameWithCompletedBatchcodeColumn = completedBatchcodeColumnAdder.addCompletedBatchcodeColumn(tableByPartialBatchcode)

        # Then
        assert_frame_equal(
            dataFrameWithCompletedBatchcodeColumn,
            TestHelper.createDataFrame(
                columns = pd.MultiIndex.from_tuples(
                            names =   ['Country',        'Region'],
                            tuples = [['United Kingdom', 'England']]),
                data = [              [4711]],
                index = pd.MultiIndex.from_tuples(
                        names =   ['Batchcode Search Term', 'Completed Batchcode'],
                        tuples = [['30L20B',                '30L20B_COMPLETION']])))
        