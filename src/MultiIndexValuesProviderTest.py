import unittest
from MultiIndexValuesProvider import MultiIndexValuesProvider
import pandas as pd

class MultiIndexValuesProviderTest(unittest.TestCase):

    def test_getValues(self):
        # Given
        value1 = '1808982'
        value2 = 'EW0175'
        value3 = 'EW0176'
        multiIndex = pd.MultiIndex.from_tuples(
            names =   ['VAX_LOT1', 'VAX_LOT2'],
            tuples = [[value1,     value2],
                      [value1,     value3]])
                        
        # When
        values = MultiIndexValuesProvider.getValues(multiIndex)

        # Then
        self.assertEqual(values, {value1, value2, value3})
