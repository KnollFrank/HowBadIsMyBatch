import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from CountryCountsByBatchcodeTable2JsonConverter import CountryCountsByBatchcodeTable2JsonConverter

class CountryCountsByBatchcodeTable2JsonConverterTest(unittest.TestCase):

    def test_convertCountryCountsByBatchcodeTable2Json(self):
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
        jsonTable = CountryCountsByBatchcodeTable2JsonConverter.convert2Json(countryCountsByBatchcodeTable)

        # Then
        assert_frame_equal(
            jsonTable,
            TestHelper.createDataFrame(
                columns = ['HISTOGRAM_DESCRIPTION'],
                data = [
                        [
                            {
                                "countries":                   ["Germany", "Hungary"],
                                "frequencies guessed":         [10,        15],
                                "frequencies before deletion": [20,        30]
                            }
                        ],
                        [
                            {
                                "countries":                   ["Germany"],
                                "frequencies guessed":         [70],
                                "frequencies before deletion": [80]
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
