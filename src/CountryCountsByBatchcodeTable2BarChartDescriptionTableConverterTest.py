import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from CountryCountsByBatchcodeTable2BarChartDescriptionTableConverter import CountryCountsByBatchcodeTable2BarChartDescriptionTableConverter

class CountryCountsByBatchcodeTable2BarChartDescriptionTableConverterTest(unittest.TestCase):

    def test_convert2BarChartDescriptionTable(self):
        # Given
        countryCountsByBatchcodeTable = TestHelper.createDataFrame(
                columns = ['COUNTRY_COUNT_BY_VAX_LOT Clicked', 'COUNTRY_COUNT_BY_VAX_LOT Before Deletion'],
                data = [  [10,                                 20],
                          [15,                                 30],
                          [70,                                 80]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',   'COUNTRY'],
                            tuples = [('!D0181',    'Germany'),
                                      ('!D0181',    'Hungary'),
                                      ('# 009C01A', 'Germany')]))
        
        # When
        barChartDescriptionTable = CountryCountsByBatchcodeTable2BarChartDescriptionTableConverter.convert2BarChartDescriptionTable(countryCountsByBatchcodeTable)

        # Then
        assert_frame_equal(
            barChartDescriptionTable,
            TestHelper.createDataFrame(
                columns = ['BAR_CHART_DESCRIPTION'],
                data = [
                        [
                            {
                                'countries':                   ['Germany', 'Hungary'],
                                'frequencies guessed':         [10,        15],
                                'frequencies before deletion': [20,        30]
                            }
                        ],
                        [
                            {
                                'countries':                   ['Germany'],
                                'frequencies guessed':         [70],
                                'frequencies before deletion': [80]
                            }
                        ]
                       ],
                index = pd.Index(
                    [
                        '!D0181',
                        '# 009C01A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)
