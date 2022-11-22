def getCountries(internationalVaersCovid19):
    return sorted(internationalVaersCovid19['COUNTRY'].unique())


def getCountryOptions(countries):
    return ['<option value="Global" selected>Global</option>'] + _getCountryOptions(countries)


def _getCountryOptions(countries):
    return [_getCountryOption(country) for country in countries]


def _getCountryOption(country):
    return '<option value="{country}">{country}</option>'.format(country=country)
