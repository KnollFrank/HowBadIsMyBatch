import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.PrrSeriesFactory import PrrSeriesFactory

class PrrSeriesFactoryTest(unittest.TestCase):

    def test_getPrrByVaccineBySymptom(self):
        # Given
        prrByVaccineAndSymptom = TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency', '17-hydroxyprogesterone'],
                data = [  [0.6,                              1.5],
                          [0.3,                              3.0]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ADEN'
                        ]))
        
        # When
        prrByVaccineBySymptom = PrrSeriesFactory.getPrrByVaccineBySymptom(prrByVaccineAndSymptom)
        
        # Then
        assert_series_equal(
            prrByVaccineBySymptom,
            pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'6VAX-F': 0.6, 'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5, 'ADEN': 3.0}
                }))

    def test_getPrrBySymptomByVaccine(self):
        # Given
        prrByVaccineAndSymptom = TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency', '17-hydroxyprogesterone'],
                data = [  [0.6,                              1.5],
                          [1.3,                              2.5]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ADEN'
                        ]))
        
        # When
        prrBySymptomByVaccine = PrrSeriesFactory.getPrrBySymptomByVaccine(prrByVaccineAndSymptom)
        
        # Then
        assert_series_equal(
            prrBySymptomByVaccine,
            TestHelper.createSeries(
                indexName = 'VAX_TYPE',
                data = {
                    '6VAX-F': {'11-beta-hydroxylase deficiency': 0.6, '17-hydroxyprogesterone': 1.5},
                    'ADEN':   {'11-beta-hydroxylase deficiency': 1.3, '17-hydroxyprogesterone': 2.5}
                }))
