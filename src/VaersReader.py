from CountryColumnAdder import CountryColumnAdder
from VaersDescrReader import VaersDescrReader
from DataFrameJoinAndDeduplicate import DataFrameJoinAndDeduplicate
from SevereColumnAdder import SevereColumnAdder

def getVaersForYears(dataDir, years):
    def addCountryColumn(dataFrame):
        dataFrame['COUNTRY'] = 'United States'
        return dataFrame

    return _getVaers(
        VaersDescrReader(dataDir).readVaersDescrsForYears(years),
        addCountryColumn)

def getNonDomesticVaers(dataDir):
    return _getVaers(
        [VaersDescrReader(dataDir).readNonDomesticVaersDescr()],
        addCountryColumn = lambda dataFrame: CountryColumnAdder(dataFrame).addCountryColumn(dataFrame))

def _getVaers(vaersDescrs, addCountryColumn):
    dataFrame = DataFrameJoinAndDeduplicate.mergeListOfDataframesAndDeduplicateByIndex(_as_VAERSDATA_VAERSVAX_Pairs(vaersDescrs))
    dataFrame = addCountryColumn(dataFrame)
    dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
    return dataFrame

def _as_VAERSDATA_VAERSVAX_Pairs(vaersDescrs):
    return [(vaersDescr['VAERSDATA'], vaersDescr['VAERSVAX']) for vaersDescr in vaersDescrs]