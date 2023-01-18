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
        RECVDATE = pd.to_datetime('01/01/2023', format = "%m/%d/%Y")
        dataFrameExpected = TestHelper.createDataFrame(
            columns = ['RECVDATE', 'DIED', 'L_THREAT', 'ER_VISIT', 'HOSPITAL', 'DISABLE', 'SPLTTYPE'],
            data = [  [RECVDATE,   np.nan,  np.nan,    np.nan,     np.nan,     np.nan,    np.nan]],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[2547730]))
        assert_frame_equal(vaersDescr['VAERSDATA'], dataFrameExpected, check_dtype=False)
