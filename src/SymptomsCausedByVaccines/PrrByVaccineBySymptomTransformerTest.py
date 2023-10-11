import unittest
from pandas.testing import assert_series_equal
import pandas as pd
from SymptomsCausedByVaccines.PrrByVaccineBySymptomTransformer import PrrByVaccineBySymptomTransformer

class PrrByVaccineBySymptomTransformerTest(unittest.TestCase):

    def test_filterByNonZeroPrrs(self):
        # Given
        prrByVaccineBySymptom = pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'6VAX-F': 0.0, 'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5, 'ADEN': 0.0}
                })
        
        # When
        prrByVaccineBySymptomWithoutZeroPrrs = PrrByVaccineBySymptomTransformer.removeNonZeroPrrs(prrByVaccineBySymptom)
        
        # Then
        assert_series_equal(
            prrByVaccineBySymptomWithoutZeroPrrs,
            pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5}
                }))
