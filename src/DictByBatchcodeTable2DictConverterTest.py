import unittest
import json
from DictByBatchcodeTable2DictConverter import DictByBatchcodeTable2DictConverter
from TestHelper import TestHelper
import pandas as pd

class DictByBatchcodeTable2DictConverterTest(unittest.TestCase):

    def test_convertDictByBatchcodeTable2Json(self):
        # Given
        dictByBatchcodeTable = TestHelper.createDataFrame(
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
                          ]
                        ],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2', 'VAX_LOT3'],
                    tuples = [['1808982',  'EW0175',   'FD1921'],
                              ['015M20A',  '1808982',  'nan']]))

        # When
        dict = DictByBatchcodeTable2DictConverter.convertDictByBatchcodeTable2Dict(dictByBatchcodeTable, '1808982')

        # Then
        self.assertEqual(
            dict,
                {
                    "batchcode": "1808982",
                    "histograms": [
                        {
                            "batchcodes": ["1808982", "EW0175", "FD1921"],
                            "histogram": {
                                "Blood pressure orthostatic abnormal": 5,
                                "Chest discomfort": 1
                            }
                        },
                        {
                            "batchcodes": ["015M20A", "1808982"],
                            "histogram": {
                                "Chest discomfort": 2
                            }
                        }
                    ]
                })
