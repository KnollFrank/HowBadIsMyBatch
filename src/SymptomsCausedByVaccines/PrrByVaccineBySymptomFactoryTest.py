import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.PrrByVaccineBySymptomFactory import PrrByVaccineBySymptomFactory

class PrrByVaccineBySymptomFactoryTest(unittest.TestCase):

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
        prrByVaccineBySymptom = PrrByVaccineBySymptomFactory.getPrrByVaccineBySymptom(prrByVaccineAndSymptom)
        
        # Then
        assert_series_equal(
            prrByVaccineBySymptom,
            pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'6VAX-F': 0.6, 'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5, 'ADEN': 3.0}
                }))
