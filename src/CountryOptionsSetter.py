from bs4 import BeautifulSoup


class CountryOptionsSetter:

    def setCountryOptions(self, html, options):
        soup = self._setCountryOptions(self._parse(html), self._parseOptions(options))
        return str(soup)

    def _setCountryOptions(self, soup, options):
        countrySelect = soup.find(id = "countrySelect")
        countrySelect.clear()
        for option in options:
            countrySelect.append(option)
        return soup

    def _parseOptions(self, options):
        return [self._parse(option).option for option in options]

    def _parse(self, html):
        return BeautifulSoup(html, 'lxml')
