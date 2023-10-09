import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.Analyzer import Analyzer

class AnalyzerTest(unittest.TestCase):

    # input a vaccine name, and see which symptoms are strongest for it.
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

