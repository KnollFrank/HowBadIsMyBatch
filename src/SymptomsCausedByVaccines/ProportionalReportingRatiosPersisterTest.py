import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
import simplejson as json
from SymptomsCausedByVaccines.ProportionalReportingRatiosPersister import saveProportionalReportingRatios


class ProportionalReportingRatiosPersisterTest(unittest.TestCase):

    def test_saveProportionalReportingRatios(self):
        # Given
        prrBySymptom = {'Sepsis ': 366.3084378480811}
        prrBySymptomByDrug = TestHelper.createSeries(
                indexName = 'DRUG',
                data = {
                    '"GENERIC COLD ACID" ': prrBySymptom
                })
        
        # When
        saveProportionalReportingRatios(prrBySymptomByDrug, 'src/tmp/vaccines')
        
        # Then
        data = ProportionalReportingRatiosPersisterTest.readJsonFile('src/tmp/vaccines/"GENERIC COLD ACID" .json')
        self.assertDictEqual(data, prrBySymptom)

    @staticmethod
    def readJsonFile(file):
        with open(file) as fp:
            return json.load(fp)
