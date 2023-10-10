from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.Analyzer import Analyzer
from SymptomsCausedByVaccines.HtmlUtils import getVaccineOptions
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(symptomByVaccine, htmlFile, lastUpdated):
    vaccineOptions = getVaccineOptions(Analyzer(symptomByVaccine).getVaccines())
    _saveVaccineOptions(vaccineOptions, htmlFile)
    saveLastUpdated2HtmlFile(lastUpdated, htmlFile)

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

# FK-TODO: DRY with src/BatchCodeTableHtmlUpdater.py
def saveLastUpdated2HtmlFile(lastUpdated, htmlFile):
    def setLastUpdated(soup):
        soup.find(id="last_updated").string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = htmlFile,
        soupTransformer = setLastUpdated)
