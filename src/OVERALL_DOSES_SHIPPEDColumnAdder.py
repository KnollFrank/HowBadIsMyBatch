import pandas as pd

# FK-TODO: DRY with ADRColumnAdder
class OVERALL_DOSES_SHIPPEDColumnAdder:
    
    def __init__(self, OVERALL_DOSES_SHIPPED_by_LOT_NUMBER):
        self.OVERALL_DOSES_SHIPPED_by_LOT_NUMBER = OVERALL_DOSES_SHIPPED_by_LOT_NUMBER

    def addColumn(self, vaccineDistributionByZipcode):
        return pd.merge(
            vaccineDistributionByZipcode,
            self.OVERALL_DOSES_SHIPPED_by_LOT_NUMBER,
            how = 'left',
            left_on = 'LOT_NUMBER',
            right_index = True,
            validate = 'many_to_one')
