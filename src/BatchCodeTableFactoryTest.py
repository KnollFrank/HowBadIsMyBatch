import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from TestHelper import TestHelper
from SevereColumnAdder import SevereColumnAdder
from BatchCodeTableFactory import BatchCodeTableFactory

class BatchCodeTableFactoryTest(unittest.TestCase):

    def test_createBatchCodeTableByCountry(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES', 'SPLTTYPE',                  'HOSPITAL', 'ER_VISIT', 'COUNTRY'],
            data = [  [1,      0,          0,         'COVID19',  'PFIZER\BIONTECH',  '016M20A', '2',               'GBPFIZER INC2020486806',    0,          0,          'United Kingdom'],
                      [0,      0,          0,         'COVID19',  'MODERNA',          '030L20A', '1',               'FRMODERNATX, INC.MOD20224', 1,          0,          'France'],
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
        batchCodeTable = batchCodeTableFactory.createBatchCodeTableByCountry('France')

        # Then
        assert_frame_equal(
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality'],
                data = [  [2,                          1,        2,              2,                            0,                  'MODERNA', 2/2 * 100,        1/2 * 100],
                          [1,                          0,        0,              0,                            1,                  'MODERNA', 0/1 * 100,        0/1 * 100]],
                index = pd.Index(
                    [
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)

    def test_createGlobalBatchCodeTable(self):
        # Given
        dataFrame = TestHelper.createDataFrame(
            columns = ['DIED', 'L_THREAT', 'DISABLE', 'VAX_TYPE', 'VAX_MANU',         'VAX_LOT', 'VAX_DOSE_SERIES', 'SPLTTYPE',                  'HOSPITAL', 'ER_VISIT', 'COUNTRY'],
            data = [  [1,      0,          0,         'COVID19',  'PFIZER\BIONTECH',  '016M20A', '2',               'dummy',                     0,          0,          None],
                      [0,      0,          0,         'COVID19',  'MODERNA',          '030L20A', '1',               'FRMODERNATX, INC.MOD20224', 0,          0,          'France'],
                      [1,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 1,          0,          'France'],
                      [0,      1,          1,         'COVID19',  'MODERNA',          '030L20B', '1',               'FRMODERNATX, INC.MOD20224', 1,          0,          'United Kingdom']],
            index = [
                "1048786",
                "1048786",
                "4711",
                "0815"])
        dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
        batchCodeTableFactory = BatchCodeTableFactory(dataFrame)
        
        # When
        batchCodeTable = batchCodeTableFactory.createGlobalBatchCodeTable()

        # Then
        assert_frame_equal(
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company',         'Severe reports', 'Lethality'],
                data = [  [1,                          1,        0,              0,                            0,                  'PFIZER\BIONTECH', 1/1 * 100,        1/1 * 100],
                          [2,                          1,        2,              2,                            2,                  'MODERNA',         2/2 * 100,        1/2 * 100],
                          [1,                          0,        0,              0,                            0,                  'MODERNA',         0/1 * 100,        0/1 * 100]],
                index = pd.Index(
                    [
                        '016M20A',
                        '030L20B',
                        '030L20A'
                    ],
                    name = 'VAX_LOT')),
            check_dtype = True)

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
            batchCodeTable[['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality']],
            TestHelper.createDataFrame(
                columns = ['Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life-Threatening Illnesses', 'Hospitalizations', 'Company', 'Severe reports', 'Lethality'],
                data = [  ],
                index = pd.Index([], name = 'VAX_LOT')),
            check_dtype = False)
