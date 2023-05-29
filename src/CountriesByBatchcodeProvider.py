import pandas as pd
from BatchCodeTableFactory import BatchCodeTableFactory
from InternationalVaersCovid19Provider import getInternationalVaersCovid19


def getCountryCountsByBatchcodeTable():
    return _combineCountryCountsByBatchcodeTables(
        countryCountsByClickedBatchcode = _getCountryCountsByClickedBatchcode(),
        countryCountsByBatchcodeBeforeDeletion = _getCountryCountsByBatchcodeBeforeDeletion())


def _getCountryCountsByClickedBatchcode():
    exploration = pd.read_csv('data/Country By Clicked Batchcode.csv', index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
    exploration.index.name = 'VAX_LOT'
    exploration.rename(
        columns =
        {
            'Country': 'COUNTRY',
            'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
        },
        inplace = True)
    exploration.set_index('COUNTRY',append = True, inplace = True)
    return exploration


def _getCountryCountsByBatchcodeBeforeDeletion():
    internationalVaersCovid19 = getInternationalVaersCovid19(dataDir = 'VAERS/VAERSBeforeDeletion', years = [2020, 2021, 2022])
    return (internationalVaersCovid19
            .groupby('VAX_LOT')
            ['COUNTRY'].value_counts()
            .to_frame(name = 'COUNTRY_COUNT_BY_VAX_LOT'))


def _combineCountryCountsByBatchcodeTables(countryCountsByClickedBatchcode, countryCountsByBatchcodeBeforeDeletion):
    countryCountsByBatchcode = pd.merge(
        countryCountsByClickedBatchcode,
        countryCountsByBatchcodeBeforeDeletion,
        how = 'outer',
        left_index = True,
        right_index = True,
        suffixes=(' Clicked', ' Before Deletion'))
    countryCountsByBatchcode.fillna(0, inplace = True)
    for column in countryCountsByBatchcode.columns:
        countryCountsByBatchcode[column] = countryCountsByBatchcode[column].astype('int64')
    return countryCountsByBatchcode


def getCountriesByBatchcodeBeforeDeletion():
    internationalVaersCovid19 = getInternationalVaersCovid19(dataDir = 'VAERS/VAERSBeforeDeletion', years = [2020, 2021, 2022])
    batchCodeTable = BatchCodeTableFactory(internationalVaersCovid19).createGlobalBatchCodeTable(countriesAsList = True)
    return batchCodeTable[['Countries']]
