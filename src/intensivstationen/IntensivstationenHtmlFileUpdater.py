from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from KreisOptionsSetter import KreisOptionsSetter


def saveKreisOptions(kreisOptions, toHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file = toHtmlFile,
        soupTransformer =
            lambda soup:
                BeautifulSoup(
                    KreisOptionsSetter().setKreisOptions(html = str(soup), options = kreisOptions),
                    'lxml'))
