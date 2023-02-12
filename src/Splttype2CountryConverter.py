import pycountry

class Splttype2CountryConverter:
    
    @staticmethod
    def convertSplttype2Country(dataFrame_SPLTTYPE_By_VAERS_ID):
        dataFrame_COUNTRY_By_VAERS_ID = dataFrame_SPLTTYPE_By_VAERS_ID[['SPLTTYPE']].copy()
        dataFrame_COUNTRY_By_VAERS_ID['COUNTRY'] = Splttype2CountryConverter._splttype2Country(dataFrame_COUNTRY_By_VAERS_ID['SPLTTYPE'])
        dataFrame_COUNTRY_By_VAERS_ID = dataFrame_COUNTRY_By_VAERS_ID.drop(columns = ['SPLTTYPE'])
        return dataFrame_COUNTRY_By_VAERS_ID

    @staticmethod
    def _splttype2Country(splttypeSeries):
        return (splttypeSeries
                .apply(
                    lambda splttype:
                        Splttype2CountryConverter._getCountryNameOfSplttypeOrDefault(
                            splttype = splttype,
                            default = 'Unknown Country'))
                .astype("string"))

    @staticmethod
    def _getCountryNameOfSplttypeOrDefault(splttype, default):
        if not isinstance(splttype, str):
            return default
        
        country = pycountry.countries.get(alpha_2 = splttype[:2])
        return country.name if country is not None else default