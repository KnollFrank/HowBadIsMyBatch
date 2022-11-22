import pycountry

class CountryColumnAdder:
    
    @staticmethod
    def addCountryColumn(dataFrame):
        dataFrame['COUNTRY'] = CountryColumnAdder.getCountryColumn(dataFrame)
        return dataFrame.astype({'COUNTRY': "string"})

    @staticmethod
    def getCountryColumn(dataFrame):
        return dataFrame.apply(
            lambda row:
                CountryColumnAdder._getCountryNameOfSplttypeOrDefault(
                 splttype = row['SPLTTYPE'],
                 default = 'Unknown Country'),
            axis = 'columns')

    @staticmethod
    def _getCountryNameOfSplttypeOrDefault(splttype, default):
        if not isinstance(splttype, str):
            return default
        
        country = pycountry.countries.get(alpha_2 = splttype[:2])
        return country.name if country is not None else default