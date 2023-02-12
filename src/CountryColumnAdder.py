import pandas as pd
from Splttype2CountryConverter import Splttype2CountryConverter

class CountryColumnAdder:
    
    def __init__(self, dataFrame_SPLTTYPE_By_VAERS_ID):
        self.dataFrame_COUNTRY_By_VAERS_ID = Splttype2CountryConverter.convertSplttype2Country(dataFrame_SPLTTYPE_By_VAERS_ID)
        
    def addCountryColumn(self, dataFrame):
        return pd.merge(
            dataFrame,
            self.dataFrame_COUNTRY_By_VAERS_ID,
            how = 'left',
            left_index = True,
            right_index = True)
    