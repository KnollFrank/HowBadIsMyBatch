import unittest
import json
from DictByBatchcodeTable2JsonConverter import DictByBatchcodeTable2JsonConverter
from TestHelper import TestHelper
import pandas as pd

class DictByBatchcodeTable2JsonConverterTest(unittest.TestCase):

    def test_convertDictByBatchcodeTable2Json(self):
        # Given
        batchcode = '1808982'
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
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [[batchcode,  'EW0175'],
                              ['015M20A',  batchcode]]))

        # When
        jsonActual = DictByBatchcodeTable2JsonConverter.convertDictByBatchcodeTable2Json(dictByBatchcodeTable, batchcode)

        # Then
        self.assertEqual(
            json.loads(jsonActual),
            json.loads('''
                {
                    "batchcode": "1808982",
                    "histograms": [
                        {
                            "batchcodes": ["1808982", "EW0175"],
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
                }'''))
