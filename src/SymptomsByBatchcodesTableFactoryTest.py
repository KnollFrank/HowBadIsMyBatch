import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from SymptomsByBatchcodesTableFactory import SymptomsByBatchcodesTableFactory
import pandas as pd
import numpy as np

class SymptomsByBatchcodesTableFactoryTest(unittest.TestCase):

    def test_createSymptomsByBatchcodesTable(self):
        # Given
        VAERSVAX = TestHelper.createDataFrame(
            columns = ['VAX_TYPE', 'VAX_MANU',        'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  ['COVID19',  'JANSSEN',         '1808982', 'UNK'],
                      ['COVID19',  'PFIZER\BIONTECH', 'EW0175',  '1']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547730]),
            dtypes = {
                'VAX_DOSE_SERIES': 'string',
                'VAX_LOT': 'string'})
        VAERSSYMPTOMS = TestHelper.createDataFrame(
            columns = ['SYMPTOM1',                            'SYMPTOM2',                'SYMPTOM3',        'SYMPTOM4',                   'SYMPTOM5'],
            data = [  ['Blood pressure orthostatic abnormal', 'COVID-19',                'Coma',            'Computerised tomogram',      'Exposure to SARS-CoV-2'],
                      ['Head injury',                         'Headache',                'Laboratory test', 'Magnetic resonance imaging', 'SARS-CoV-2 antibody test negative'],
                      ['SARS-CoV-2 test positive',            'Unresponsive to stimuli', 'X-ray',           np.nan,                       np.nan]],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547730,
                        2547730]))
                
        # When
        symptomsByBatchcodesTable = SymptomsByBatchcodesTableFactory.createSymptomsByBatchcodesTable(VAERSVAX, VAERSSYMPTOMS)

        # Then
        assert_frame_equal(
            symptomsByBatchcodesTable,
            TestHelper.createDataFrame(
                columns = ['Blood pressure orthostatic abnormal', 'COVID-19', 'Coma', 'Computerised tomogram', 'Exposure to SARS-CoV-2', 'Head injury', 'Headache', 'Laboratory test', 'Magnetic resonance imaging', 'SARS-CoV-2 antibody test negative', 'SARS-CoV-2 test positive', 'Unresponsive to stimuli', 'X-ray'],
                data = [  [1,                                     1,          1,      1,                        1,                        1,             1,         1,                 1,                            1,                                   1,                          1,                         1]],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982',  'EW0175']])))
