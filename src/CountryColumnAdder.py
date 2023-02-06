import pycountry

class CountryColumnAdder:
    
    @staticmethod
    def addCountryColumn(dataFrame):
        dataFrame['COUNTRY'] = CountryColumnAdder._splttype2Country(dataFrame['SPLTTYPE'])
        return dataFrame

    @staticmethod
    def _splttype2Country(splttypeSeries):
        return (splttypeSeries
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