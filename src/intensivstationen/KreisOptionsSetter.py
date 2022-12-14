from bs4 import BeautifulSoup


class KreisOptionsSetter:

    def setKreisOptions(self, html, options):
        soup = self._setKreisOptions(self._parse(html), self._parseOptions(options))
        return str(soup)

    def _setKreisOptions(self, soup, options):
        kreisSelect = soup.find(id = "kreisSelect")
        kreisSelect.clear()
        for option in options:
            kreisSelect.append(option)
        return soup

    def _parseOptions(self, options):
        return [self._parse(option).option for option in options]

    def _parse(self, html):
        return BeautifulSoup(html, 'lxml')
