from DataFrameFilter import DataFrameFilter
from VaersReader import getVaersForYears, getNonDomesticVaers
import pandas as pd

def getInternationalVaersCovid19(years):
    internationalVaers = pd.concat([getVaersForYears(years), getNonDomesticVaers()])
    internationalVaersCovid19 = DataFrameFilter().filterByCovid19(internationalVaers)
    return internationalVaersCovid19