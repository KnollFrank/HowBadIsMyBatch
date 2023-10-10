from bs4 import BeautifulSoup


class OptionsSetter:

    def setOptions(self, html, options):
        soup = self._setBatchcodeOptions(self._parse(html), self._parseOptions(options))
        return str(soup)

    def _setBatchcodeOptions(self, soup, options):
        batchcodeSelect = soup.find(id = "vaccineSelect")
        batchcodeSelect.clear()
        for option in options:
            batchcodeSelect.append(option)
        return soup

    def _parseOptions(self, options):
        return [self._parse(option).option for option in options]

    def _parse(self, html):
        return BeautifulSoup(html, 'lxml')
