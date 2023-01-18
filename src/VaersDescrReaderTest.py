import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from VaersDescrReader import VaersDescrReader
import pandas as pd
import numpy as np

class VaersDescrReaderTest(unittest.TestCase):

    def test_readVaersDescrForYear(self):
        # Given
        vaersDescrReader = VaersDescrReader(dataDir = "src/testdata")

        # When
        vaersDescr = vaersDescrReader.readVaersDescrForYear(2023)

        # Then
        assert_frame_equal(
                vaersDescr['VAERSDATA'],
                TestHelper.createDataFrame(
                    columns = ['RECVDATE',                                          'DIED', 'L_THREAT', 'ER_VISIT', 'HOSPITAL', 'DISABLE', 'SPLTTYPE'],
                    data = [  [pd.to_datetime('01/01/2023', format = "%m/%d/%Y"),   np.nan,  np.nan,    np.nan,     np.nan,     np.nan,    np.nan]],
                    index = pd.Index(
                            name = 'VAERS_ID',
                            data=[2547730])),
                check_dtype = False)
        assert_frame_equal(
                vaersDescr['VAERSVAX'],
                TestHelper.createDataFrame(
                    columns = ['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
                    data = [  ['COVID19',  'JANSSEN',  '1808982', 'UNK']],
                    index = pd.Index(
                            name = 'VAERS_ID',
                            data=[2547730])),
                check_dtype = False)
