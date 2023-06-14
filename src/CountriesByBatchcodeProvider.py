import pandas as pd
from InternationalVaersCovid19Provider import getInternationalVaersCovid19BeforeDeletion
from CountryCountsByBatchcodeTablesMerger import CountryCountsByBatchcodeTablesMerger


def getCountryCountsByBatchcodeTable():
    return _combineCountryCountsByBatchcodeTables(
        countryCountsByClickedBatchcode = CountryCountsByBatchcodeTablesMerger.getCountryCountsByClickedBatchcodeTable(),
        countryCountsByBatchcodeBeforeDeletion = _getCountryCountsByBatchcodeBeforeDeletion())


def _getCountryCountsByBatchcodeBeforeDeletion():
    return (getInternationalVaersCovid19BeforeDeletion()
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


def getDateRangeOfVAERSReports(internationalVaersCovid19):
    dates = internationalVaersCovid19['RECVDATE']
    return dates.min(), dates.max()


def filterByBatchcodes(countryCountsByBatchcode, batchcodes2Retain):
    return countryCountsByBatchcode.loc[(batchcodes2Retain, slice(None)), :]