import unittest
from MultiIndexValuesProvider import MultiIndexValuesProvider
import pandas as pd

class MultiIndexValuesProviderTest(unittest.TestCase):

    def test_getValues(self):
        # Given
        multiIndex = pd.MultiIndex.from_tuples(
            names =   ['VAX_LOT1', 'VAX_LOT2'],
            tuples = [['1808982',  'EW0175'],
                      ['1808982',  'EW0176']])
                        
        # When
        values = MultiIndexValuesProvider.getValues(multiIndex)

        # Then
        self.assertEqual(values, {'1808982', 'EW0175', 'EW0176'})
