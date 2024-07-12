import unittest
from pandas.testing import assert_series_equal
from TestHelper import TestHelper
import pandas as pd
import simplejson as json
from SymptomsCausedByVaccines.ProportionalReportingRatiosPersister import saveProportionalReportingRatios


class ProportionalReportingRatiosPersisterTest(unittest.TestCase):

    def test_saveProportionalReportingRatios(self):
        # Given
        drug = '"GENERIC COLD ACID" '
        prrBySymptom = { 'Sepsis ': 366.3084378480811 }
        prrBySymptomByDrug = TestHelper.createSeries(
                indexName = 'DRUG',
                data = { drug: prrBySymptom })
        directory = 'src/tmp/vaccines'
        
        # When
        filenameByDrug = saveProportionalReportingRatios(prrBySymptomByDrug, directory)
        
        # Then
        drugFilename = '1'
        self.assertDictEqual(
            ProportionalReportingRatiosPersisterTest.readJsonFile(f'{directory}/{drugFilename}.json'),
            prrBySymptom)
        self.assertDictEqual(filenameByDrug, { drug: drugFilename })

    @staticmethod
    def readJsonFile(file):
        with open(file) as fp:
            return json.load(fp)
