import pandas as pd
from CompanyColumnAdder import CompanyColumnAdder
from SummationTableFactory import SummationTableFactory

class BatchCodeTableFactory:

    def __init__(self, dataFrame: pd.DataFrame):
        self.dataFrame = dataFrame
    
    def createGlobalBatchCodeTable(self):
        return self._postProcess(SummationTableFactory.createSummationTable(self.dataFrame.groupby('VAX_LOT')))

    def createBatchCodeTableByCountry(self, country):
        return self._postProcess(self._getBatchCodeTableByCountry(country))

    def _postProcess(self, batchCodeTable):
        batchCodeTable = CompanyColumnAdder(self.dataFrame).addCompanyColumn(batchCodeTable)
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
        countryBatchCodeTable = self._getCountryBatchCodeTable()
        return countryBatchCodeTable.loc[country] if country in countryBatchCodeTable.index else self._getEmptyBatchCodeTable(countryBatchCodeTable)

    def _getCountryBatchCodeTable(self):
        return SummationTableFactory.createSummationTable(
            self.dataFrame.groupby(
                [
                    self.dataFrame['COUNTRY'],
                    self.dataFrame['VAX_LOT']
                ]))

    def _getEmptyBatchCodeTable(self, countryBatchCodeTable):
        return countryBatchCodeTable[0:0].droplevel(0)
