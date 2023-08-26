import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from BarChartDescriptionTables import BarChartDescriptionTables

class BarChartDescriptionTablesTest(unittest.TestCase):

    def test_filterValidJensenShannonDistances(self):
        # Given
        barChartDescriptionTable = TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION'],
                data = [
                        [
                            {
                                'countries':                        ['Germany', 'Hungary'],
                                'Adverse Reaction Reports guessed': [0,         0],
                                'Adverse Reaction Reports known':   [20,        30],
                                'Jensen-Shannon distance':          np.nan
                            }
                        ],
                        [
                            {
                                'countries':                        ['Germany'],
                                'Adverse Reaction Reports guessed': [70],
                                'Adverse Reaction Reports known':   [80],
                                'Jensen-Shannon distance':          0.4711
                            }
                        ]
                       ],
                index = pd.Index(
                    [
                        '!D0181',
                        '# 009C01A'
                    ],
                    name = 'VAX_LOT'))
        
        # When
        barChartDescriptionTableResult = BarChartDescriptionTables.filterValidJensenShannonDistances(barChartDescriptionTable)

        # Then
        assert_frame_equal(
            barChartDescriptionTableResult,
            TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION'],
                data = [
                        [
                            {
                                'countries':                        ['Germany'],
                                'Adverse Reaction Reports guessed': [70],
                                'Adverse Reaction Reports known':   [80],
                                'Jensen-Shannon distance':          0.4711
                            }
                        ]
                       ],
                index = pd.Index(
                    [
                        '# 009C01A',
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
