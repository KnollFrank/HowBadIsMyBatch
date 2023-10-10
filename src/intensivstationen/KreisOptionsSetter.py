from bs4 import BeautifulSoup
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


class KreisOptionsSetter:

    def setKreisOptions(self, html, options):
        return OptionsSetter().setOptions(html, 'kreisSelect', options)
