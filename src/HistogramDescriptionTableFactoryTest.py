import unittest
from pandas.testing import assert_frame_equal
from HistogramDescriptionTableFactory import HistogramDescriptionTableFactory
from TestHelper import TestHelper
import pandas as pd

class HistogramDescriptionTableFactoryTest(unittest.TestCase):

    def test_createHistogramDescriptionTable(self):
        # Given
        dictByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['SYMPTOM_COUNT_BY_VAX_LOT'],
                data = [  [{"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}],
                          [{"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}],
                          [{"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}],

                          [{"Chest discomfort": 2}],
                          [{"Chest discomfort": 2}],
                          [{"Chest discomfort": 2}]
                        ],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT_EXPLODED', 'VAX_LOT1', 'VAX_LOT2', 'VAX_LOT3'],
                    tuples = [['1808982',          '1808982',  'EW0175',   'FD1921'],
                              ['EW0175',           '1808982',  'EW0175',   'FD1921'],
                              ['FD1921',           '1808982',  'EW0175',   'FD1921'],

                              ['015M20A',          '015M20A',  '1808982',  'nan'],
                              ['1808982',          '015M20A',  '1808982',  'nan'],
                              ['nan',              '015M20A',  '1808982',  'nan']]))

        # When
        histogramDescriptionTable = HistogramDescriptionTableFactory.createHistogramDescriptionTable(dictByBatchcodeTable)

        # Then
        assert_frame_equal(
            histogramDescriptionTable,
            TestHelper.createDataFrame(
                columns = ['HISTOGRAM_DESCRIPTION'],
                data = [  [
                            {
                                "batchcode": "1808982",
                                "histograms": [
                                    {
                                        "batchcodes": ["1808982", "EW0175", "FD1921"],
                                        "histogram": {"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}
                                    },
                                    {
                                        "batchcodes": ["015M20A", "1808982"],
                                        "histogram": {"Chest discomfort": 2}
                                    }
                                ]
                            }
                          ],
                          [
                            {
                                "batchcode": "EW0175",
                                "histograms": [
                                    {
                                        "batchcodes": ["1808982", "EW0175", "FD1921"],
                                        "histogram": {"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}
                                    }
                                ]
                            }
                          ],
                          [
                            {
                                "batchcode": "FD1921",
                                "histograms": [
                                    {
                                        "batchcodes": ["1808982", "EW0175", "FD1921"],
                                        "histogram": {"Blood pressure orthostatic abnormal": 5, "Chest discomfort": 1}
                                    }
                                ]
                            }
                          ],
                          [
                            {
                                "batchcode": "015M20A",
                                "histograms": [
                                    {
                                        "batchcodes": ["015M20A", "1808982"],
                                        "histogram": {"Chest discomfort": 2}
                                    }
                                ]
                            }
                          ]
                        ],
                index =  pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        '1808982',
                        'EW0175',
                        'FD1921',
                        '015M20A'])),
            check_like = True)
