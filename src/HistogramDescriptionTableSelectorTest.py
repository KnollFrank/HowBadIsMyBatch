import unittest
from pandas.testing import assert_frame_equal
from HistogramDescriptionTableSelector import HistogramDescriptionTableSelector
from TestHelper import TestHelper
import pandas as pd

class HistogramDescriptionTableSelectorTest(unittest.TestCase):

    def test_selectHistogramsWithShortestBatchcodeCombinations(self):
        # Given
        histogramDescriptionTable = TestHelper.createDataFrame(
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
                          ]
                        ],
                index =  pd.Index(
                    name = 'VAX_LOT',
                    data = ['1808982']))

        # When
        histogramsWithShortestBatchcodeCombinationsTable = HistogramDescriptionTableSelector.selectHistogramsWithShortestBatchcodeCombinations(histogramDescriptionTable)

        # Then
        assert_frame_equal(
            histogramsWithShortestBatchcodeCombinationsTable,
            TestHelper.createDataFrame(
                columns = ['HISTOGRAM_DESCRIPTION'],
                data = [  [
                            {
                                "batchcode": "1808982",
                                "histogram": {"Chest discomfort": 2}
                            }
                          ]
                        ],
                index =  pd.Index(
                    name = 'VAX_LOT',
                    data = ['1808982'])))
        