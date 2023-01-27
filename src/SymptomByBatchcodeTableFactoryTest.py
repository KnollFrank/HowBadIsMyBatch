import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from SymptomByBatchcodeTableFactory import SymptomByBatchcodeTableFactory
import pandas as pd
import numpy as np

class SymptomByBatchcodeTableFactoryTest(unittest.TestCase):

    def test_createSymptomByBatchcodeTable(self):
        # Given
        VAERSVAX = TestHelper.createDataFrame(
            columns = ['VAX_TYPE', 'VAX_MANU',        'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  ['COVID19',  'JANSSEN',         'EW0175',  'UNK'],
                      ['COVID19',  'PFIZER\BIONTECH', '1808982', '1']],
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
        symptomByBatchcodeTable = SymptomByBatchcodeTableFactory.createSymptomByBatchcodeTable(VAERSVAX, VAERSSYMPTOMS)

        # Then
        assert_frame_equal(
            symptomByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM'],
                data = [  ['Blood pressure orthostatic abnormal'],
                          ['Head injury'],
                          ['SARS-CoV-2 test positive'],
                          ['COVID-19'],
                          ['Headache'],
                          ['Unresponsive to stimuli'],
                          ['Coma'],
                          ['Laboratory test'],
                          ['X-ray'],
                          ['Computerised tomogram'],
                          ['Magnetic resonance imaging'],
                          ['Exposure to SARS-CoV-2'],
                          ['SARS-CoV-2 antibody test negative']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982', 'EW0175']] * 13)))

    def test_createSymptomByBatchcodeTable_two_patients_same_symptoms(self):
        # Given
        VAERSVAX = TestHelper.createDataFrame(
            columns = ['VAX_TYPE', 'VAX_MANU', 'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  ['COVID19',  'JANSSEN',  'EW0175',  '1'],
                      ['COVID19',  'JANSSEN',  'EW0175',  '1']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547731]),
            dtypes = {
                'VAX_DOSE_SERIES': 'string',
                'VAX_LOT': 'string'})
        VAERSSYMPTOMS = TestHelper.createDataFrame(
            columns = ['SYMPTOM1',                           'SYMPTOM2', 'SYMPTOM3', 'SYMPTOM4', 'SYMPTOM5'],
            data = [  ['Blood pressure orthostatic abnormal', np.nan,    np.nan,     np.nan,     np.nan],
                      ['Blood pressure orthostatic abnormal', np.nan,    np.nan,     np.nan,     np.nan]],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547731]))
                
        # When
        symptomByBatchcodeTable = SymptomByBatchcodeTableFactory.createSymptomByBatchcodeTable(VAERSVAX, VAERSSYMPTOMS)

        # Then
        assert_frame_equal(
            symptomByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM'],
                data = [  ['Blood pressure orthostatic abnormal'],
                          ['Blood pressure orthostatic abnormal']],
                index = pd.Index(
                    name = 'VAX_LOT1',
                    data = ['EW0175',
                            'EW0175'])),
                check_dtype = False)

    def test_createSymptomByBatchcodeTable_two_patients_distinct_symptoms(self):
        # Given
        VAERSVAX = TestHelper.createDataFrame(
            columns = ['VAX_TYPE', 'VAX_MANU',        'VAX_LOT', 'VAX_DOSE_SERIES'],
            data = [  ['COVID19',  'JANSSEN',         '1808982', 'UNK'],
                      ['COVID19',  'PFIZER\BIONTECH', 'EW0175',  '1'],
                      ['COVID19',  'PFIZER\BIONTECH', 'EW0175',  '1'],
                      ['COVID19',  'PFIZER\BIONTECH', 'EW0167',  '2']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547730,
                        2547744,
                        2547744]),
            dtypes = {
                'VAX_DOSE_SERIES': 'string',
                'VAX_LOT': 'string'})
        VAERSSYMPTOMS = TestHelper.createDataFrame(
            columns = ['SYMPTOM1',                            'SYMPTOM2',                        'SYMPTOM3',        'SYMPTOM4',                             'SYMPTOM5'],
            data = [  ['Blood pressure orthostatic abnormal', 'COVID-19',                        'Coma',            'Computerised tomogram',                'Exposure to SARS-CoV-2'],
                      ['Head injury',                         'Headache',                        'Laboratory test', 'Magnetic resonance imaging',           'SARS-CoV-2 antibody test negative'],
                      ['SARS-CoV-2 test positive',            'Unresponsive to stimuli',         'X-ray',           np.nan,                                 np.nan],
                      ['Computerised tomogram head abnormal', 'Ear pain',                        'Headache',        'Idiopathic intracranial hypertension', 'Intracranial pressure increased'],
                      ['Lumbar puncture',                     'Magnetic resonance imaging head', 'Pain',            'Swelling',                             'Vision blurred']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data=[
                        2547730,
                        2547730,
                        2547730,
                        2547744,
                        2547744]))
                
        # When
        symptomByBatchcodeTable = SymptomByBatchcodeTableFactory.createSymptomByBatchcodeTable(VAERSVAX, VAERSSYMPTOMS)

        # Then
        assert_frame_equal(
            symptomByBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['SYMPTOM'],
                data = [  ['Blood pressure orthostatic abnormal'],
                          ['Head injury'],
                          ['SARS-CoV-2 test positive'],
                          ['COVID-19'],
                          ['Headache'],
                          ['Unresponsive to stimuli'],
                          ['Coma'],
                          ['Laboratory test'],
                          ['X-ray'],
                          ['Computerised tomogram'],
                          ['Magnetic resonance imaging'],
                          ['Exposure to SARS-CoV-2'],
                          ['SARS-CoV-2 antibody test negative'],
                          
                          ['Computerised tomogram head abnormal'],
                          ['Lumbar puncture'],
                          ['Ear pain'],
                          ['Magnetic resonance imaging head'],
                          ['Headache'],
                          ['Pain'],
                          ['Idiopathic intracranial hypertension'],
                          ['Swelling'],
                          ['Intracranial pressure increased'], 
                          ['Vision blurred']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['1808982',  'EW0175']] * 13 + [['EW0167', 'EW0175']] * 10)))
