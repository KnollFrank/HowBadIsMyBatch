import pycountry
import pandas as pd

class CountryColumnAdder:
    
    def __init__(self, dataFrame_SPLTTYPE_By_VAERS_ID):
        self.dataFrame_COUNTRY_By_VAERS_ID = self._create_dataFrame_COUNTRY_By_VAERS_ID(dataFrame_SPLTTYPE_By_VAERS_ID)
        
    def addCountryColumn(self, dataFrame):
        return pd.merge(
            dataFrame,
            self.dataFrame_COUNTRY_By_VAERS_ID,
            how = 'left',
            left_index = True,
            right_index = True)

    def _create_dataFrame_COUNTRY_By_VAERS_ID(self, dataFrame_SPLTTYPE_By_VAERS_ID):
        dataFrame_COUNTRY_By_VAERS_ID = dataFrame_SPLTTYPE_By_VAERS_ID[['SPLTTYPE']].copy()
        dataFrame_COUNTRY_By_VAERS_ID['COUNTRY'] = self._splttype2Country(dataFrame_COUNTRY_By_VAERS_ID['SPLTTYPE'])
        dataFrame_COUNTRY_By_VAERS_ID = dataFrame_COUNTRY_By_VAERS_ID.drop(columns = ['SPLTTYPE'])
        return dataFrame_COUNTRY_By_VAERS_ID

    def _splttype2Country(self, splttypeSeries):
        return (splttypeSeries
                .apply(
                    lambda splttype:
                        self._getCountryNameOfSplttypeOrDefault(
                            splttype = splttype,
                            default = 'Unknown Country'))
                .astype("string"))

    def _getCountryNameOfSplttypeOrDefault(self, splttype, default):
        if not isinstance(splttype, str):
            return default
        
        country = pycountry.countries.get(alpha_2 = splttype[:2])
        return country.name if country is not None else default