import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from SymptomsCausedByVaccines.MultiLineFitting.SymptomCombinationsProvider import SymptomCombinationsProvider

class SymptomCombinationsProviderTest(unittest.TestCase):

    def test_generateSymptomCombinations(self):
        # Given
        prrByLotAndSymptom = TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomB', 'SymptomC', 'SymptomD'],
                data = [  [0.6,        1.5,        1.2,        0.0]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1'
                        ]))
        
        # When
        symptomCombinations = list(
            SymptomCombinationsProvider.generateSymptomCombinations(
                prrByLotAndSymptom,
                dataFramePredicate = lambda df: len(df) >= 1))
        
        # Then
        self.assertEqual(len(symptomCombinations), 3)
        assert_frame_equal(
            symptomCombinations[0],
            TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomB'],
                data = [  [0.6,        1.5]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1'
                        ])))
        assert_frame_equal(
            symptomCombinations[1],
            TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomC'],
                data = [  [0.6,        1.2]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1'
                        ])))
        assert_frame_equal(
            symptomCombinations[2],
            TestHelper.createDataFrame(
                columns = ['SymptomB', 'SymptomC'],
                data = [  [1.5,        1.2]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1'
                        ])))

    def test_generateSymptomCombinations_minSizeOfDataFrame_2(self):
        # Given
        prrByLotAndSymptom = TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomB'],
                data = [  [0.6,        1.5],
                          [1.6,        2.5]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1',
                        'LOT-2'
                        ]))
        
        # When
        symptomCombinations = list(
            SymptomCombinationsProvider.generateSymptomCombinations(
                prrByLotAndSymptom,
                dataFramePredicate = lambda df: len(df) >= 2))
        
        # Then
        self.assertEqual(len(symptomCombinations), 1)
        assert_frame_equal(
            symptomCombinations[0],
            TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomB'],
                data = [  [0.6,        1.5],
                          [1.6,        2.5]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1',
                        'LOT-2'
                        ])))

    def test_generateSymptomCombinations_minSizeOfDataFrame_3(self):
        # Given
        prrByLotAndSymptom = TestHelper.createDataFrame(
                columns = ['SymptomA', 'SymptomB'],
                data = [  [0.6,        1.5],
                          [1.6,        2.5]],
                index = pd.Index(
                    name = 'VAX_LOT',
                    data = [
                        'LOT-1',
                        'LOT-2'
                        ]))
        
        # When
        symptomCombinations = list(
            SymptomCombinationsProvider.generateSymptomCombinations(
                prrByLotAndSymptom,
                dataFramePredicate = lambda df: len(df) >= 3))
        
        # Then
        self.assertEqual(len(symptomCombinations), 0)
