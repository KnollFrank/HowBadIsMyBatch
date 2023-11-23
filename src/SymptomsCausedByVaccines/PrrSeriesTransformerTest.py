import unittest
from pandas.testing import assert_series_equal
import pandas as pd
from SymptomsCausedByVaccines.PrrSeriesTransformer import PrrSeriesTransformer

class PrrSeriesTransformerTest(unittest.TestCase):

    def test_filterByNonZeroPrrs(self):
        # Given
        prrByVaccineBySymptom = pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'6VAX-F': 0.0, 'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5, 'ADEN': 0.0}
                })
        
        # When
        prrByVaccineBySymptomWithoutZeroPrrs = PrrSeriesTransformer.filterByNonZeroPrrs(prrByVaccineBySymptom)
        
        # Then
        assert_series_equal(
            prrByVaccineBySymptomWithoutZeroPrrs,
            pd.Series(
                {
                    '11-beta-hydroxylase deficiency': {'ADEN': 0.3},
                    '17-hydroxyprogesterone': {'6VAX-F': 1.5}
                }))

    def test_filterPrrs(self):
        # Given
        prrBySymptomByVaccine = pd.Series(
                {
                    '6VAX-F': {'11-beta-hydroxylase deficiency': 2.6, '17-hydroxyprogesterone': 1.5},
                    'ADEN':   {'11-beta-hydroxylase deficiency': 1.3, '17-hydroxyprogesterone': 2.9}
                })
        
        # When
        prrBySymptomByVaccineWithHighPrrs = PrrSeriesTransformer.filterPrrs(prrBySymptomByVaccine, lambda prr: prr >= 2)
        
        # Then
        assert_series_equal(
            prrBySymptomByVaccineWithHighPrrs,
            pd.Series(
                {
                    '6VAX-F': {'11-beta-hydroxylase deficiency': 2.6},
                    'ADEN':   {'17-hydroxyprogesterone': 2.9}
                }))
