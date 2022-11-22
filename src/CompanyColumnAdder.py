import pandas as pd

class CompanyColumnAdder:
    
    def __init__(self, dataFrame_VAX_LOT_VAX_MANU):
        self.dataFrame_VAX_LOT_VAX_MANU = dataFrame_VAX_LOT_VAX_MANU

    def addCompanyColumn(self, batchCodeTable):
        return pd.merge(
            batchCodeTable,
            self._createCompanyByBatchCodeTable(),
            how = 'left',
            left_index = True,
            right_index = True,
            validate = 'one_to_one')

    def _createCompanyByBatchCodeTable(self):
        manufacturerByBatchCodeTable = self.dataFrame_VAX_LOT_VAX_MANU[['VAX_LOT', 'VAX_MANU']]
        manufacturerByBatchCodeTable = manufacturerByBatchCodeTable.drop_duplicates(subset = ['VAX_LOT'])
        manufacturerByBatchCodeTable = manufacturerByBatchCodeTable.set_index('VAX_LOT')
        return manufacturerByBatchCodeTable.rename(columns = {"VAX_MANU": "Company"})