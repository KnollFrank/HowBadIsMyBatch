import unittest
from pandas.testing import assert_frame_equal
from MultiIndexExploder import MultiIndexExploder
from TestHelper import TestHelper
import pandas as pd

class MultiIndexExploderTest(unittest.TestCase):

    def test_explodeMultiIndexOfTable(self):
        # Given
        table = TestHelper.createDataFrame(
                columns = ['DATA'],
                data = [  ['A, B data'],
                          ['C, A data'],
                          ['C, B data']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['A',        'B'],
                              ['C',        'A'],
                              ['C',        'B']]))

        # When
        explodedTable = MultiIndexExploder.explodeMultiIndexOfTable(table)

        # Then
        assert_frame_equal(
            explodedTable,
            TestHelper.createDataFrame(
                columns = ['DATA'],
                data = [  ['A, B data'],
                          ['A, B data'],

                          ['C, A data'],
                          ['C, A data'],
                          
                          ['C, B data'],
                          ['C, B data']],
                index = pd.MultiIndex.from_tuples(
                    names =   ['VAX_LOT_EXPLODED', 'VAX_LOT1', 'VAX_LOT2'],
                    tuples = [['A',                'A',        'B'],
                              ['B',                'A',        'B'],

                              ['C',                'C',        'A'],
                              ['A',                'C',        'A'],

                              ['C',                'C',        'B'],                              
                              ['B',                'C',        'B']])))
