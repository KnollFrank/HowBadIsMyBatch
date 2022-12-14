from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from KreisOptionsSetter import KreisOptionsSetter
from HtmlTransformerUtil import HtmlTransformerUtil


def saveLastUpdatedIntensivstationen(lastUpdated, toHtmlFile):
    def setLastUpdated(soup):
        soup.find(id = "Datenstand").string.replace_with(lastUpdated.strftime(DateProvider.INTENSIVSTATIONEN_DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = toHtmlFile,
        soupTransformer = setLastUpdated)


def saveKreisOptions(kreisOptions, toHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file = toHtmlFile,
        soupTransformer =
            lambda soup:
                BeautifulSoup(
                    KreisOptionsSetter().setKreisOptions(html = str(soup), options = kreisOptions),
                    'lxml'))
