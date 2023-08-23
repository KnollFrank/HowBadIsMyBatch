import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from JensenShannonDistance2BarChartDescriptionColumnAdder import JensenShannonDistance2BarChartDescriptionColumnAdder
from scipy.spatial import distance

class JensenShannonDistance2BarChartDescriptionColumnAdderTest(unittest.TestCase):

    def test_addJensenShannonDistance2BarChartDescriptionColumn(self):
        # Given
        barChartDescriptionTable = TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION'],
                data = [
                        [
                            {
                                'countries':                        ['Germany', 'Hungary'],
                                'Adverse Reaction Reports guessed': [10,        15],
                                'Adverse Reaction Reports known':   [20,        30]
                            }
                        ]
                       ],
                index = pd.Index(
                    [
                        '!D0181',
                    ],
                    name = 'VAX_LOT'))
        
        # When
        barChartDescriptionTableWithJensenShannonDistance = JensenShannonDistance2BarChartDescriptionColumnAdder.addJensenShannonDistance2BarChartDescriptionColumn(barChartDescriptionTable)

        # Then
        assert_frame_equal(
            barChartDescriptionTableWithJensenShannonDistance,
            TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION'],
                data = [
                        [
                            {
                                'countries':                        ['Germany', 'Hungary'],
                                'Adverse Reaction Reports guessed': [10,        15],
                                'Adverse Reaction Reports known':   [20,        30],
                                'Jensen-Shannon distance':          distance.jensenshannon([10, 15], [20, 30], base = 2.0)
                            }
                        ]
                       ],
                index = pd.Index(
                    [
                        '!D0181',
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
