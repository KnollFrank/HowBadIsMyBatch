import pandas as pd

class ADRColumnAdder:
    
    def __init__(self, ADR_by_Batchcode):
        self.ADR_by_Batchcode = ADR_by_Batchcode

    def addADRColumn(self, vaccineDistributionByZipcode):
        return pd.merge(
            vaccineDistributionByZipcode,
            self.ADR_by_Batchcode,
            how = 'left',
            left_on = 'LOT_NUMBER',
            right_index = True,
            validate = 'many_to_one')
