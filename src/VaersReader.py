from CountryColumnAdder import CountryColumnAdder
from VaersDescrReader import VaersDescrReader
from VaersDescr2DataFrameConverter import VaersDescr2DataFrameConverter
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
    dataFrame = VaersDescr2DataFrameConverter.createDataFrameFromDescrs(vaersDescrs)
    dataFrame = addCountryColumn(dataFrame)
    dataFrame = SevereColumnAdder.addSevereColumn(dataFrame)
    return dataFrame