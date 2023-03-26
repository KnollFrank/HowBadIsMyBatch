class CountriesColumnAdder:

    def addCountriesColumn(self, countriesByBatchcodeTable):
        countriesByBatchcodeTable['Countries'] = countriesByBatchcodeTable.apply(self._getCountriesHavingEvents, axis='columns')
        return countriesByBatchcodeTable

    def _getCountriesHavingEvents(self, eventCountByCountry):
        return set(eventCountByCountry[eventCountByCountry > 0].index)
