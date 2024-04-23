import unittest
from pandas.testing import assert_frame_equal
from VaersDescr2DataFrameConverter import VaersDescr2DataFrameConverter
from TestHelper import TestHelper
from DataFrameFilter import DataFrameFilter

class DataFrameFilterTest(unittest.TestCase):

    def test_filterByCovid19(self):
        # Given
        dataFrame = VaersDescr2DataFrameConverter.createDataFrameFromDescrs(
            [
                {
                    'VAERSDATA': TestHelper.createDataFrame(
                        columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL'],
                        data = [  [1,      0,          0,         1],
                                  [0,      0,          1,         0]],
                        index = [
                            "0916600",
                            "0916601"]),
                    'VAERSVAX': TestHelper.createDataFrame(
                        columns = ['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
                        data = [  ['COVID19',  'MODERNA',  '037K20A', '1'],
                                  ['COVID19',  'MODERNA',  '025L20A', '1']],
                        index = [
                            "0916600",
                            "0916601"],
                        dtypes = {"VAX_DOSE_SERIES": "string"})
                },
                {
                    'VAERSDATA': TestHelper.createDataFrame(
                        columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL'],
                        data = [  [0,       0,         0,         0],
                                  [0,       0,         1,         0]],
                            index = [
                            "1996873",
                            "1996874"]),
                    'VAERSVAX': TestHelper.createDataFrame(
                            columns = ['VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES'],
                            data = [  ['HPV9',     'MERCK & CO. INC.', 'R017624', 'UNK'],
                                      ['COVID19',  'MODERNA',          '025L20A', '1']],
                            index = [
                                "1996873",
                                "1996874"],
                            dtypes = {"VAX_DOSE_SERIES": "string"})
                    }
            ])
        dataFrameFilter = DataFrameFilter()
            
        # When
        dataFrame = dataFrameFilter.filterByCovid19(dataFrame)
        
        # Then
        dataFrameExpected = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL', 'VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  [1,       0,         0,         1,          'COVID19',  'MODERNA',  '037K20A', '1'],
                      [0,       0,         1,         0,          'COVID19',  'MODERNA',  '025L20A', '1'],
                      [0,       0,         1,         0,          'COVID19',  'MODERNA',  '025L20A', '1']],
            index = [
                "0916600",
                "0916601",
                "1996874"],
            dtypes = {"VAX_DOSE_SERIES": "string"})
        assert_frame_equal(dataFrame, dataFrameExpected, check_dtype = False)
