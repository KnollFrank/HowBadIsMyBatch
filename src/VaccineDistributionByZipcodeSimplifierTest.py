import unittest
from VaccineDistributionByZipcodeSimplifier import VaccineDistributionByZipcodeSimplifier
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd

class VaccineDistributionByZipcodeSimplifierTest(unittest.TestCase):

    def test_sumDoses(self):
        # Given
        vaccineDistributionByZipcode = TestHelper.createDataFrame(
            columns = ['PROVIDER_NAME',            'ZIPCODE_SHP', 'LOT_NUMBER', 'DOSES_SHIPPED'],
            data = [  ['@PHARMACY.COM',            '97206-2314',  'FK9893',     300.0],
                      ['@PHARMACY.COM - 82ND AVE', '97266-4885',  'FK9893',     300.0],
                      ['@PHARMACY.COM - 82ND AVE', '97266-4885',  'FK9893',     400.0],
                      ['@PHARMACY.COM - 82ND AVE', '97266-4885',  'FL8095',     200.0]])
                        
        # When
        vaccineDistributionByZipcodeSimplified = VaccineDistributionByZipcodeSimplifier.sumDoses(vaccineDistributionByZipcode)

        # Then
        assert_frame_equal(
            vaccineDistributionByZipcodeSimplified,
            TestHelper.createDataFrame(
            columns = ['PROVIDER_NAME',            'ZIPCODE_SHP', 'LOT_NUMBER', 'DOSES_SHIPPED'],
            data = [  ['@PHARMACY.COM',            '97206-2314',  'FK9893',     300.0],
                      ['@PHARMACY.COM - 82ND AVE', '97266-4885',  'FK9893',     700.0],
                      ['@PHARMACY.COM - 82ND AVE', '97266-4885',  'FL8095',     200.0]]))
