import pycountry

class CountryColumnAdder:
    
    @staticmethod
    def addCountryColumn(dataFrame):
        dataFrame['COUNTRY'] = CountryColumnAdder._getCountryColumn(dataFrame)
        return dataFrame

    @staticmethod
    def _getCountryColumn(dataFrame):
        return (dataFrame['SPLTTYPE']
                .apply(
                    lambda splttype:
                        CountryColumnAdder._getCountryNameOfSplttypeOrDefault(
                            splttype = splttype,
                            default = 'Unknown Country'))
                .astype("string"))

    @staticmethod
    def _getCountryNameOfSplttypeOrDefault(splttype, default):
        if not isinstance(splttype, str):
            return default
        
        country = pycountry.countries.get(alpha_2 = splttype[:2])
        return country.name if country is not None else default