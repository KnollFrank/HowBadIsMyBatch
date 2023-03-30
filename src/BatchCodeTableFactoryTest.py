import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from SevereColumnAdder import SevereColumnAdder
from BatchCodeTableFactory import BatchCodeTableFactory

class BatchCodeTableFactoryTest(unittest.TestCase):

    def test_createBatchCodeTableByCountry_countriesAsStr(self):
        self._createBatchCodeTableByCountry(countriesAsList = False)

    def test_createBatchCodeTableByCountry_countriesAsList(self):
        self._createBatchCodeTableByCountry(countriesAsList = True)

    def test_createGlobalBatchCodeTable(self):
        self._createGlobalBatchCodeTable(countriesAsList = False)

    def test_createGlobalBatchCodeTable_countriesAsList(self):
        self._createGlobalBatchCodeTable(countriesAsList = True)

    def test_createBatchCodeTableByNonExistingCountry(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES', 'SPLTTYPE',                  'HOSPITAL', 'ER_VISIT', 'COUNTRY'],
            data = [  [1,      0,          0,         'COVID19',  'PFIZER\BIONTECH',  '016M20A', '2',               'GBPFIZER INC2020486806',    0,          0,          'United Kingdom'],
                      [0,      0,          0,         'COVID19',  'MODERNA',          '030L20A', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [1,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [0,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France']],
            index = [
                "1048786",
                "1048786",
                "4711",
                "0815"])
        dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
        batchCodeTableFactory = BatchCodeTableFactory(dataFrame)
        
        # When
        batchCodeTable = batchCodeTableFactory.createBatchCodeTableByCountry('non existing country')

        # Then
        assert_frame_equal(
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Countries', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Countries', 'Severe reports', 'Lethality'],
                data = [  ],
                index = pd.Index([], name = 'VAX_LOT')),
            check_dtype = False)

    def _createBatchCodeTableByCountry(self, countriesAsList):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES', 'SPLTTYPE',                  'HOSPITAL', 'ER_VISIT', 'COUNTRY'],
            data = [  [1,      0,          0,         'COVID19',  'PFIZER\BIONTECH',  '016M20A', '2',               'GBPFIZER INC2020486806',    0,          0,          'United Kingdom'],
                      [0,      0,          0,         'COVID19',  'MODERNA',          '030L20A', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [1,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [0,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France']],
            index = [
                "1048786",
                "1048786",
                "4711",
                "0815"])
        dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
        batchCodeTableFactory = BatchCodeTableFactory(dataFrame)
        
        # When
        batchCodeTable = batchCodeTableFactory.createBatchCodeTableByCountry('France', countriesAsList)

        # Then
        france = self._convertCountries(['France'], countriesAsList)
        assert_frame_equal(
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Countries', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Countries', 'Severe reports', 'Lethality'],
                data = [  [2,                          1,        2,              2,                            'MODERNA', france,      2/2 * 100,        1/2 * 100],
                          [1,                          0,        0,              0,                            'MODERNA', france,      0/1 * 100,        0/1 * 100]],
                index = pd.Index(
                    [
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)

    def _createGlobalBatchCodeTable(self, countriesAsList):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES', 'SPLTTYPE',                  'HOSPITAL', 'ER_VISIT', 'COUNTRY'],
            data = [  [1,      0,          0,         'COVID19',  'PFIZER\BIONTECH',  '016M20A', '2',               'GBPFIZER INC2020486806',    0,          0,          'United Kingdom'],
                      [0,      0,          0,         'COVID19',  'MODERNA',          '030L20A', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [1,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [0,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'United Kingdom']],
            index = [
                "1048786",
                "1048786",
                "4711",
                "0815"])
        dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
        batchCodeTableFactory = BatchCodeTableFactory(dataFrame)
        
        # When
        batchCodeTable = batchCodeTableFactory.createGlobalBatchCodeTable(countriesAsList)

        # Then
        assert_frame_equal(
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Countries', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company',         'Countries',                                                           'Severe reports', 'Lethality'],
                data = [  [1,                          1,        0,              0,                            'PFIZER\BIONTECH', self._convertCountries(['United Kingdom'], countriesAsList),           1/1 * 100,        1/1 * 100],
                          [2,                          1,        2,              2,                            'MODERNA',         self._convertCountries(['France', 'United Kingdom'], countriesAsList), 2/2 * 100,        1/2 * 100],
                          [1,                          0,        0,              0,                            'MODERNA',         self._convertCountries(['France'], countriesAsList),                   0/1 * 100,        0/1 * 100]],
                index = pd.Index(
                    [
                        '016M20A',
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)

    def _convertCountries(self, countries, countriesAsList):
        return ', '.join(countries) if not countriesAsList else countries            
