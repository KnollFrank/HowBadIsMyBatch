from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.HtmlUtils import getSymptomOptions
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(symptoms, htmlFile):    
    _saveOptions(
        options = getSymptomOptions(symptoms),
        htmlFile = htmlFile,
        selectElementId = 'symptomSelect')
    
def _saveOptions(options, htmlFile, selectElementId):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=htmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                OptionsSetter().setOptions(
                    html = str(soup),
                    selectElementId = selectElementId,
                    options = options),
                'lxml'))

# FK-TODO: move saveLastUpdated2HtmlFile() to src/BatchCodeTableHtmlUpdater.py
def saveLastUpdated2HtmlFile(lastUpdated, htmlFile, lastUpdatedElementId):
    def setLastUpdated(soup):
        soup.find(id = lastUpdatedElementId).string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = htmlFile,
        soupTransformer = setLastUpdated)
