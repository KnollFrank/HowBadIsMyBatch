from DataFrameFilter import DataFrameFilter
import VaersReader
import pandas as pd
from VaersDescrReader import VaersDescrReader


def getInternationalVaersCovid19(years):
    internationalVaers = pd.concat(
        [
            VaersReader.getVaersForYears(years),
            VaersReader.getNonDomesticVaers()
        ])
    internationalVaersCovid19 = DataFrameFilter().filterByCovid19(internationalVaers)
    return internationalVaersCovid19


def get_international_VAERSVAX_VAERSSYMPTOMS_Covid19(years):
    international_VAERSVAX, international_VAERSSYMPTOMS = _get_international_VAERSVAX_VAERSSYMPTOMS(years)
    international_VAERSVAX.dropna(subset = ['VAX_LOT'], inplace = True)
    international_VAERSVAX_Covid19 = DataFrameFilter().filterByCovid19(international_VAERSVAX)
    return international_VAERSVAX_Covid19, international_VAERSSYMPTOMS


def _get_international_VAERSVAX_VAERSSYMPTOMS(years):
    vaersDescrReader = VaersDescrReader(dataDir = "VAERS")
    internationalVaersDescrs = vaersDescrReader.readVaersDescrsForYears(years) + [vaersDescrReader.readNonDomesticVaersDescr()]
    return _getVaersDescrByName(internationalVaersDescrs, 'VAERSVAX'), _getVaersDescrByName(internationalVaersDescrs, 'VAERSSYMPTOMS')


def _getVaersDescrByName(vaersDescrs, vaersDescrName):
    return pd.concat([vaersDescr[vaersDescrName] for vaersDescr in vaersDescrs])
