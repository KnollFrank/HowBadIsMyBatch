import unittest
from TestHelper import TestHelper
from pandas.testing import assert_frame_equal
import pandas as pd
from CountryColumnAdder import CountryColumnAdder


class CountryColumnAdderTest(unittest.TestCase):
    
    def test_addCountryColumn(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['SPLTTYPE'],
            data = [  ['GBPFIZER INC2020486806'],
                      ['FRMODERNATX, INC.MOD20224'],
                      ['dummy']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data = [
                        "4711",
                        "0815",
                        "123"]))
        countryColumnAdder = CountryColumnAdder(dataFrame)

        # When
        dataFrameWithCountryColumn = countryColumnAdder.addCountryColumn(dataFrame)

        # Then
        assert_frame_equal(
            dataFrameWithCountryColumn,
            TestHelper.createDataFrame(
                columns = ['SPLTTYPE',                  'COUNTRY'],
                data = [  ['GBPFIZER INC2020486806',    'United Kingdom'],
                          ['FRMODERNATX, INC.MOD20224', 'France'],
                          ['dummy',                     None]],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            "4711",
                            "0815",
                            "123"]),
                dtypes = {'COUNTRY': 'string'}))


    def test_addCountryColumn2(self):
        # Given
        countryColumnAdder = CountryColumnAdder(
            TestHelper.createDataFrame(
                columns = ['SPLTTYPE'],
                data = [  ['GBPFIZER INC2020486806'],
                          ['FRMODERNATX, INC.MOD20224'],
                          ['dummy']],
                index = pd.Index(
                    name = 'VAERS_ID',
                    data = [
                        2547744,
                        2547730,
                        2540815])))
        dataFrame = TestHelper.createDataFrame(
            columns = ['VAX_LOT'],
            data = [  ['1808982'],
                      ['EW0175'],
                      ['EW0176']],
            index = pd.Index(
                    name = 'VAERS_ID',
                    data = [
                        2547730,
                        2547730,
                        2547744]))
        
        # When
        dataFrameWithCountryColumn = countryColumnAdder.addCountryColumn(dataFrame)

        # Then
        assert_frame_equal(
            dataFrameWithCountryColumn,
            TestHelper.createDataFrame(
                columns = ['VAX_LOT', 'COUNTRY'],
                data = [  ['1808982', 'France'],
                          ['EW0175',  'France'],
                          ['EW0176',  'United Kingdom']],
                index = pd.Index(
                        name = 'VAERS_ID',
                        data = [
                            2547730,
                            2547730,
                            2547744]),
                dtypes = {'COUNTRY': 'string'}))
