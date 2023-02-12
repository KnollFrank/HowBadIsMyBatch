from CountryColumnAdder import CountryColumnAdder
from VaersDescrReader import VaersDescrReader
from VaersDescr2DataFrameConverter import VaersDescr2DataFrameConverter
from SevereColumnAdder import SevereColumnAdder

def getVaersForYears(years):
    def addCountryColumn(dataFrame):
        dataFrame['COUNTRY'] = 'United States'
        return dataFrame

    return _getVaers(
        _getVaersDescrReader().readVaersDescrsForYears(years),
        addCountryColumn)

def getNonDomesticVaers():
    return _getVaers(
        [_getVaersDescrReader().readNonDomesticVaersDescr()],
        addCountryColumn = lambda dataFrame: CountryColumnAdder(dataFrame).addCountryColumn(dataFrame))

def _getVaersDescrReader():
    return VaersDescrReader(dataDir = "VAERS")

def _getVaers(vaersDescrs, addCountryColumn):
    dataFrame = VaersDescr2DataFrameConverter.createDataFrameFromDescrs(vaersDescrs)
    dataFrame = addCountryColumn(dataFrame)
    dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
    return dataFrame