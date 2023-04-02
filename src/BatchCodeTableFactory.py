import pandas as pd
from CompanyColumnAdder import CompanyColumnAdder
from SummationTableFactory import SummationTableFactory

class BatchCodeTableFactory:

    def __init__(self, dataFrame: pd.DataFrame):
        self.dataFrame = dataFrame
        self.companyColumnAdder = CompanyColumnAdder(dataFrame)
        self.countryBatchCodeTable = SummationTableFactory.createSummationTable(
            dataFrame.groupby(
                [
                    dataFrame['COUNTRY'],
                    dataFrame['VAX_LOT']
                ]))

    def createGlobalBatchCodeTable(self, countriesAsList = False):
        return self._postProcess(SummationTableFactory.createSummationTable(self.dataFrame.groupby('VAX_LOT')), countriesAsList)

    def createBatchCodeTableByCountry(self, country, countriesAsList = False):
        return self._postProcess(self._getBatchCodeTableByCountry(country), countriesAsList)

    def _postProcess(self, batchCodeTable, countriesAsList):
        batchCodeTable = self.companyColumnAdder.addCompanyColumn(batchCodeTable)
        batchCodeTable = batchCodeTable[
            [
                'Adverse Reaction Reports',
                'Deaths',
                'Disabilities',
                'Life Threatening Illnesses',
                'Company',
                'Severe reports',
                'Lethality'
            ]]
        return batchCodeTable.sort_values(by = 'Severe reports', ascending = False)

    def _getBatchCodeTableByCountry(self, country):
        if country in self.countryBatchCodeTable.index:
            return self.countryBatchCodeTable.loc[country]
        else:
            return self._getEmptyBatchCodeTable()

    def _getEmptyBatchCodeTable(self):
        return self.countryBatchCodeTable[0:0].droplevel(0)
