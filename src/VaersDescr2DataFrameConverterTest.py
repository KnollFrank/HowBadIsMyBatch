import unittest
from pandas.testing import assert_frame_equal
from VaersDescr2DataFrameConverter import VaersDescr2DataFrameConverter
from TestHelper import TestHelper

class VaersDescr2DataFrameConverterTest(unittest.TestCase):

    def test_createDataFrameFromDescr(self):
        # Given
        vaersDescr = {
                    'VAERSDATA': TestHelper.createDataFrame(
                        columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL'],
                        data = [  [1,      0,          0,         1],
                                  [0,      1,          0,         1],
                                  [0,      0,          1,         0]],
                        index = [
                            "0916600",
                            "0916600",
                            "0916601"]),
                    'VAERSVAX': TestHelper.createDataFrame(
                        columns = ['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
                        data = [  ['COVID19',  'MODERNA',  '037K20A', '1'],
                                  ['COVID19',  'MODERNA',  '037K20B', '1'],
                                  ['COVID19',  'MODERNA',  '025L20A', '1']],
                        index = [
                            "0916600",
                            "0916600",
                            "0916601"],
                        dtypes = {"VAX_DOSE_SERIES": "string"})
                }
            
        # When
        dataFrame = VaersDescr2DataFrameConverter.createDataFrameFromDescr(vaersDescr)
        
        # Then
        dataFrameExpected = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL', 'VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  [1,       0,         0,         1,          'COVID19',  'MODERNA',  '037K20A', '1'],
                      [1,       0,         0,         1,          'COVID19',  'MODERNA',  '037K20B', '1'],
                      [0,       1,         0,         1,          'COVID19',  'MODERNA',  '037K20A', '1'],
                      [0,       1,         0,         1,          'COVID19',  'MODERNA',  '037K20B', '1'],
                      [0,       0,         1,         0,          'COVID19',  'MODERNA',  '025L20A', '1']],
            index = [
                "0916600",
                "0916600",
                "0916600",
                "0916600",
                "0916601"],
            dtypes = {"VAX_DOSE_SERIES": "string"})
        assert_frame_equal(dataFrame, dataFrameExpected, check_dtype = False)
