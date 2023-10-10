from bs4 import BeautifulSoup


class OptionsSetter:

    def setOptions(self, html, selectElementId, options):
        soup = self._setOptions(self._parse(html), selectElementId, self._parseOptions(options))
        return str(soup)

    def _setOptions(self, soup, selectElementId, options):
        selectElement = soup.find(id = selectElementId)
        selectElement.clear()
        for option in options:
            selectElement.append(option)
        return soup

    def _parseOptions(self, options):
        return [self._parse(option).option for option in options]

    def _parse(self, html):
        return BeautifulSoup(html, 'lxml')
