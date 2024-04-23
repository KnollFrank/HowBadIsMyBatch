import unittest
from pandas.testing import assert_frame_equal
from BatchCodeTableIntoHistogramDescriptionTableMerger import BatchCodeTableIntoHistogramDescriptionTableMerger
from TestHelper import TestHelper
import pandas as pd
import numpy as np

class BatchCodeTableIntoHistogramDescriptionTableMergerTest(unittest.TestCase):

    def test_mergeBatchCodeTableIntoHistogramDescriptionTable(self):
        # Given
        histogramDescriptionTable = TestHelper.createDataFrame(
                columns = ['HISTOGRAM_DESCRIPTION',                                                                    'COUNTRY'],
                data = [  [
                            {
                                'batchcode': '1808982',
                                'histograms': [
                                    {
                                        'batchcodes': ['1808982', 'EW0175', 'FD1921'],
                                        'histogram': {'Blood pressure orthostatic abnormal': 5, 'Chest discomfort': 1}
                                    },
                                    {
                                        'batchcodes': ['015M20A', '1808982'],
                                        'histogram': {'Chest discomfort': 2}
                                    }
                                ]
                            },
                                                                                                                        'Global'
                          ]
                        ],
                index =  pd.Index(
                    name = 'VAX_LOT',
                    data = ['1808982']))
        
        batchCodeTable = TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality'],
                data = [  [2,                          1,        2,              2,                            3,                  'MODERNA', 2/2 * 100,        np.nan]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = ['1808982']))

        # When
        mergedTable = BatchCodeTableIntoHistogramDescriptionTableMerger().mergeBatchCodeTableIntoHistogramDescriptionTable(batchCodeTable = batchCodeTable, histogramDescriptionTable = histogramDescriptionTable)

        # Then
        assert_frame_equal(
            mergedTable,
            TestHelper.createDataFrame(
                columns = ['HISTOGRAM_DESCRIPTION',                                                                    'COUNTRY'],
                data = [  [
                            {
                                'batchcode': '1808982',
                                'Adverse Reaction Reports': 2,
                                'Deaths': 1,
                                'Disabilities': 2,
                                'Life-Threatening Illnesses': 2,
                                'Hospitalizations': 3,
                                'Company': 'MODERNA',
                                'histograms': [
                                    {
                                        'batchcodes': ['1808982', 'EW0175', 'FD1921'],
                                        'histogram': {'Blood pressure orthostatic abnormal': 5, 'Chest discomfort': 1}
                                    },
                                    {
                                        'batchcodes': ['015M20A', '1808982'],
                                        'histogram': {'Chest discomfort': 2}
                                    }
                                ]
                            },
                                                                                                                        'Global'
                          ]
                        ],
                index =  pd.Index(
                    name = 'VAX_LOT',
                    data = ['1808982'])))
