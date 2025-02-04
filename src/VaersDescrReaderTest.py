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
                    columns = ['RECVDATE',                                        'DIED', 'L_THREAT', 'ER_VISIT', 'HOSPITAL', 'DISABLE', 'VAX_DATE',                                        'SPLTTYPE'],
                    data = [  [pd.to_datetime('01/01/2023', format = "%m/%d/%Y"), 0,      0,          0,          0,          0,         pd.to_datetime('04/06/2021', format = "%m/%d/%Y"), np.nan]],
                    index = pd.Index(
                            name = 'VAERS_ID',
                            data = [2547730])))
        assert_frame_equal(
                vaersDescr['VAERSVAX'],
                TestHelper.createDataFrame(
                    columns = ['VAX_TYPE', 'VAX_MANU',        'VAX_LOT', 'VAX_DOSE_SERIES'],
                    data = [  ['COVID19',  'JANSSEN',         '1808982', 'UNK'],
                              ['COVID19',  'PFIZER\BIONTECH', 'EW0175',  '1']],
                    index = pd.Index(
                            name = 'VAERS_ID',
                            data = [
                                2547730,
                                2547730]),
                    dtypes = {
                        'VAX_DOSE_SERIES': 'string',
                        'VAX_LOT': 'string'}))
        assert_frame_equal(
                vaersDescr['VAERSSYMPTOMS'],
                TestHelper.createDataFrame(
                    columns = ['SYMPTOM1',                            'SYMPTOM2',                'SYMPTOM3',        'SYMPTOM4',                   'SYMPTOM5'],
                    data = [  ['Blood pressure orthostatic abnormal', 'COVID-19',                'Coma',            'Computerised tomogram',      'Exposure to SARS-CoV-2'],
                              ['Head injury',                         'Headache',                'Laboratory test', 'Magnetic resonance imaging', 'SARS-CoV-2 antibody test negative'],
                              ['SARS-CoV-2 test positive',            'Unresponsive to stimuli', 'X-ray',           np.nan,                       np.nan]],
                    index = pd.Index(
                            name = 'VAERS_ID',
                            data = [
                                2547730,
                                2547730,
                                2547730])))
