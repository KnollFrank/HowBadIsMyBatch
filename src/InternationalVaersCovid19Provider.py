from DataFrameFilter import DataFrameFilter
import VaersReader
import pandas as pd


def getInternationalVaersCovid19(years):
    internationalVaers = pd.concat(
        [
            VaersReader.getVaersForYears(years),
            VaersReader.getNonDomesticVaers()
        ])
    internationalVaersCovid19 = DataFrameFilter().filterByCovid19(internationalVaers)
    return internationalVaersCovid19
