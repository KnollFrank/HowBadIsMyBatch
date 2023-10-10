from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.HtmlUtils import getVaccineOptions
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(vaccines, htmlFile, lastUpdated):
    _saveVaccineOptions(
        vaccineOptions = getVaccineOptions(vaccines),
        htmlFile = htmlFile,
        vaccineSelectElementId = 'vaccineSelect')
    saveLastUpdated2HtmlFile(
        lastUpdated = lastUpdated,
        htmlFile = htmlFile,
        lastUpdatedElementId = 'last_updated')

def _saveVaccineOptions(vaccineOptions, htmlFile, vaccineSelectElementId):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=htmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                OptionsSetter().setOptions(
                    html = str(soup),
                    selectElementId = vaccineSelectElementId,
                    options = vaccineOptions),
                'lxml'))

def saveLastUpdated2HtmlFile(lastUpdated, htmlFile, lastUpdatedElementId):
    def setLastUpdated(soup):
        soup.find(id = lastUpdatedElementId).string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = htmlFile,
        soupTransformer = setLastUpdated)
