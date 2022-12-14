import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import statistics
import pandas as pd
from intensivstationen.MedianOfFreeBedsByKreisTableFactory import MedianOfFreeBedsByKreisTableFactory

class MedianOfFreeBedsByKreisTableFactoryTest(unittest.TestCase):

    def test_createMedianOfFreeBedsByKreisTable(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['date',       'betten_frei', 'betten_belegt', 'Kreis'],
            data = [  ['2020-04-24', 40,            38,              'Flensburg, Stadt'],
                      ['2020-04-24', 42,            36,              'Flensburg, Stadt'],
                      ['2020-04-24', 44,            34,              'Flensburg, Stadt'],
                      ['2020-04-24', 9,             10,              'Bamberg']],
            index = [
                0,
                1,
                2,
                3])
        medianOfFreeBedsByKreisTableFactory = MedianOfFreeBedsByKreisTableFactory(dataFrame)
        
        # When
        medianOfFreeBedsByKreisTable = medianOfFreeBedsByKreisTableFactory.createMedianOfFreeBedsByKreisTable('Kreis')

        # Then
        assert_frame_equal(
            medianOfFreeBedsByKreisTable,
            TestHelper.createDataFrame(
                columns = ['median_free_beds_in_percent'],
                data = [  [statistics.median([40/(40 + 38) * 100, 42/(42 + 36) * 100, 44/(44 + 34) * 100])],
                          [9/(9 + 10) * 100]],
                index = pd.Index(
                    name = 'Kreis',
                    data = [
                        'Flensburg, Stadt',
                        'Bamberg'
                    ])),
            check_dtype = False)