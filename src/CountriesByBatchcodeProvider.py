import pandas as pd
from BatchCodeTableFactory import BatchCodeTableFactory
from InternationalVaersCovid19Provider import getInternationalVaersCovid19
from SummationTableFactory import SummationTableFactory
from CountryCountsByBatchcodeTablesMerger import CountryCountsByBatchcodeTablesMerger


def getCountryCountsByBatchcodeTable():
    return _combineCountryCountsByBatchcodeTables(
        countryCountsByClickedBatchcode = CountryCountsByBatchcodeTablesMerger.getCountryCountsByClickedBatchcodeTable(),
        countryCountsByBatchcodeBeforeDeletion = _getCountryCountsByBatchcodeBeforeDeletion())


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


def getCountriesByClickedBatchcode():
    return (CountryCountsByBatchcodeTablesMerger
        .getCountryCountsByClickedBatchcodeTable()
        .reset_index(level = 'COUNTRY')
        .groupby('VAX_LOT')
        .agg(
            Countries =
                pd.NamedAgg(
                    column = 'COUNTRY',
                    aggfunc = SummationTableFactory.sortCountries)))


def getCountriesByBatchcodeBeforeDeletion():
    internationalVaersCovid19 = getInternationalVaersCovid19(dataDir = 'VAERS/VAERSBeforeDeletion', years = [2020, 2021, 2022])
    batchCodeTable = BatchCodeTableFactory(internationalVaersCovid19).createGlobalBatchCodeTable(countriesAsList = True)
    return batchCodeTable[['Countries']]
