from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.Analyzer import Analyzer
from SymptomsCausedByVaccines.HtmlUtils import getVaccineOptions
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(symptomByVaccine, htmlFile, lastUpdated):
    vaccineOptions = getVaccineOptions(Analyzer(symptomByVaccine).getVaccines())
    _saveVaccineOptions(vaccineOptions, htmlFile)
    saveLastUpdated2HtmlFile(
        lastUpdated = lastUpdated,
        htmlFile = htmlFile,
        lastUpdatedElementId = 'last_updated')

def _saveVaccineOptions(vaccineOptions, htmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=htmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                OptionsSetter().setOptions(
                    html = str(soup),
                    selectElementId = 'vaccineSelect',
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
