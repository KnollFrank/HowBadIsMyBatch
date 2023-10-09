import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.Analyzer import Analyzer

class AnalyzerTest(unittest.TestCase):

    def test_getSymptomsForVaccine(self):
        # Given
        symptomByVaccine = TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency', '17-hydroxyprogesterone'],
                data = [  [0.6,                              0.4]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = ['6VAX-F']))
        
        analyzer = Analyzer(symptomByVaccine)

        # When
        symptomsForVaccine = analyzer.getSymptomsForVaccine('6VAX-F')
        
        # Then
        assert_series_equal(
            symptomsForVaccine,
            pd.Series(
                name = '6VAX-F',
                data = {
                    '11-beta-hydroxylase deficiency': 0.6,
                    '17-hydroxyprogesterone': 0.4
                    }))

    def test_getVaccinesForSymptom(self):
        # Given
        symptomByVaccine = TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency'],
                data = [  [0.6],
                          [0.3]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ADEN'
                        ]))
        
        analyzer = Analyzer(symptomByVaccine)

        # When
        vaccinesForSymptom = analyzer.getVaccinesForSymptom('11-beta-hydroxylase deficiency')
        
        # Then
        assert_series_equal(
            vaccinesForSymptom,
            TestHelper.createSeries(
                name = '11-beta-hydroxylase deficiency',
                data = {
                    '6VAX-F': 0.6,
                    'ADEN': 0.3
                    },
                indexName = 'VAX_TYPE'))
