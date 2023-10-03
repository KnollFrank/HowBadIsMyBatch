import unittest
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
import pandas as pd
from src.GoogleAnalytics.RegionCountsByBatchcodeTablesMerger import RegionCountsByBatchcodeTablesMerger

class RegionCountsByBatchcodeTablesMergerTest(unittest.TestCase):

    def test_getRegionCountsByClickedBatchcode(self):
        # Given

        # When
        regionCountsByClickedBatchcodeTable = RegionCountsByBatchcodeTablesMerger.getRegionCountsByClickedBatchcode('src/testdata/GoogleAnalytics')
        
        # Then
        assert_frame_equal(
            regionCountsByClickedBatchcodeTable,
            TestHelper.createDataFrame(
                columns = ['REGION_COUNT_BY_VAX_LOT'],
                data = [  [100       + 200],
                          [(10 + 20) + (20 + 40)]],
                index = pd.MultiIndex.from_tuples(
                            names =   ['VAX_LOT',  'COUNTRY',       'REGION'],
                            tuples = [['#003B21A', 'United States', 'California'],
                                      ['000086A',  'Germany',       'Bavaria']])))
