from DataFrameFilter import DataFrameFilter
import VaersReader
import pandas as pd
from VaersDescrReader import VaersDescrReader
from CountryColumnAdder import CountryColumnAdder
from GoogleDriveDownloader import GoogleDriveDownloader

def getInternationalVaersCovid19(dataDir, years):
    internationalVaers = pd.concat(
        [
            VaersReader.getVaersForYears(dataDir, years),
            VaersReader.getNonDomesticVaers(dataDir)
        ])
    internationalVaersCovid19 = DataFrameFilter().filterByCovid19(internationalVaers)
    return internationalVaersCovid19


def getInternationalVaersCovid19BeforeDeletion():
    GoogleDriveDownloader.downloadSevenZipFileAndExtract(
        remoteSevenZipSrcFile = "https://drive.google.com/file/d/1Rb-lfxNxw_WwvRDVLEhvqOyv_a2f8ern/view?usp=drive_link",
        localSevenZipDstFile = 'VAERS/VAERSBeforeDeletion.7z')
    return getInternationalVaersCovid19(dataDir = 'VAERS/VAERSBeforeDeletion', years = [2020, 2021, 2022])

def get_international_VAERSVAX_VAERSSYMPTOMS_Covid19(years):
    VAERSDATA, VAERSVAX, VAERSSYMPTOMS = _get_VAERSDATA_VAERSVAX_VAERSSYMPTOMS(years)
    VAERSVAX_Covid19_CountryColumn = _get_VAERSVAX_Covid19_CountryColumn(VAERSVAX, CountryColumnAdder(VAERSDATA))
    return VAERSVAX_Covid19_CountryColumn, VAERSSYMPTOMS


def _get_VAERSDATA_VAERSVAX_VAERSSYMPTOMS(years):
    vaersDescrReader = VaersDescrReader(dataDir = "VAERS")
    vaersDescrs = vaersDescrReader.readVaersDescrsForYears(years) + [vaersDescrReader.readNonDomesticVaersDescr()]
    return (_getVaersDescrByName(vaersDescrs, 'VAERSDATA'),
            _getVaersDescrByName(vaersDescrs, 'VAERSVAX'),
            _getVaersDescrByName(vaersDescrs, 'VAERSSYMPTOMS'))


def _getVaersDescrByName(vaersDescrs, vaersDescrName):
    return pd.concat([vaersDescr[vaersDescrName] for vaersDescr in vaersDescrs])


def _get_VAERSVAX_Covid19_CountryColumn(VAERSVAX, countryColumnAdder):
    VAERSVAX.dropna(subset = ['VAX_LOT'], inplace = True)
    VAERSVAX_Covid19 = DataFrameFilter().filterByCovid19(VAERSVAX)
    VAERSVAX_Covid19_CountryColumn = countryColumnAdder.addCountryColumn(VAERSVAX_Covid19)
    return VAERSVAX_Covid19_CountryColumn
