import unittest
from TestHelper import TestHelper
from BatchcodeCompletion import BatchcodeCompletion
import pandas as pd

class BatchcodeCompletionTest(unittest.TestCase):

    def test_completeBatchcode(self):
        # Given
        ADR_by_Batchcode = TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports'],
                data = [  [1],
                          [200],
                          [149]],
                index = pd.Index(
                    [
                        'LOT000057A',
                        '030L20B',
                        '000057A'
                    ],
                    name = 'VAX_LOT'))
        batchcodeCompletion = BatchcodeCompletion(ADR_by_Batchcode)
                        
        # When
        completedBatchcode = batchcodeCompletion.completeBatchcode('000057')

        # Then
        self.assertEqual(completedBatchcode, '000057A')

    def test_completeBatchcode_no_completion(self):
        # Given
        ADR_by_Batchcode = TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports'],
                data = [  [1],
                          [200],
                          [149]],
                index = pd.Index(
                    [
                        'LOT000057A',
                        '030L20B',
                        '000057A'
                    ],
                    name = 'VAX_LOT'))
        batchcodeCompletion = BatchcodeCompletion(ADR_by_Batchcode)
                        
        # When
        completedBatchcode = batchcodeCompletion.completeBatchcode('non existing batch code')

        # Then
        self.assertIsNone(completedBatchcode)
