import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from JensenShannonDistanceColumnAdder import JensenShannonDistanceColumnAdder
from scipy.spatial import distance

class JensenShannonDistanceColumnAdderTest(unittest.TestCase):

    def test_addJensenShannonDistanceColumn(self):
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
        barChartDescriptionTableWithJensenShannonDistanceColumn = JensenShannonDistanceColumnAdder.addJensenShannonDistanceColumn(barChartDescriptionTable)

        # Then
        assert_frame_equal(
            barChartDescriptionTableWithJensenShannonDistanceColumn,
            TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION',                                          'JENSEN_SHANNON_DISTANCE'],
                data = [
                        [
                            {
                                'countries':                        ['Germany', 'Hungary'],
                                'Adverse Reaction Reports guessed': [10,        15],
                                'Adverse Reaction Reports known':   [20,        30]
                            },
                                                                                             distance.jensenshannon([10, 15], [20, 30], base = 2.0)
                        ]
                       ],
                index = pd.Index(
                    [
                        '!D0181',
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
