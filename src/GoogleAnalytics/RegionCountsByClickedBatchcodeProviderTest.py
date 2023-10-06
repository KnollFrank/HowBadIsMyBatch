import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from GoogleAnalytics.RegionCountsByClickedBatchcodeProvider import RegionCountsByClickedBatchcodeProvider

class RegionCountsByClickedBatchcodeProviderTest(unittest.TestCase):

    def test_getRegionCountsByClickedBatchcode(self):
        # Given

        # When
        regionCountsByClickedBatchcodeTable = RegionCountsByClickedBatchcodeProvider.getRegionCountsByClickedBatchcode('src/testdata/GoogleAnalytics/CountryByBatchcode 20230730-20230929.csv')
        
        # Then
        assert_frame_equal(
            regionCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['REGION_COUNT_BY_VAX_LOT'],
                data = [  [100],
                          [10 + 20]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION'],
                            tuples = [['#003B21A', 'United States', 'California'],
                                      ['000086A',  'Germany',       'Bavaria']])))
