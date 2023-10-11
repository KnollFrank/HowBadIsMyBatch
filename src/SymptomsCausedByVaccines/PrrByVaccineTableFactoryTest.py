import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.PrrByVaccineTableFactory import PrrByVaccineTableFactory

class PrrByVaccineTableFactoryTest(unittest.TestCase):

    def test_getPrrByVaccineTable(self):
        # Given
        prrByVaccineAndSymptom = TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency'],
                data = [  [0.6],
                          [0.3]],
                index = pd.Index(
                    name = 'VAX_TYPE',
                    data = [
                        '6VAX-F',
                        'ADEN'
                        ]))
        
        # When
        prrByVaccineTable = PrrByVaccineTableFactory.getPrrByVaccineTable(prrByVaccineAndSymptom)
        
        # Then
        assert_frame_equal(
            prrByVaccineTable,
            TestHelper.createDataFrame(
                columns = ['11-beta-hydroxylase deficiency'],
                data = [  [{'6VAX-F': 0.6, 'ADEN': 0.3}]],
                index = pd.Index(['PrrByVaccine'])))
