from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from BatchcodeOptionsSetter import BatchcodeOptionsSetter
from HtmlUtils import getBatchcodeOptions, getBatchcodes
from DateProvider import DateProvider


def updateBatchCodeTableHtmlFile(batchCodeTable, batchCodeTableHtmlFile, lastUpdated):
    batchcodeOptions = getBatchcodeOptions(getBatchcodes(batchCodeTable.sort_values(by = 'Adverse Reaction Reports', ascending = False)))
    _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile)
    saveLastUpdated2HtmlFile(lastUpdated, batchCodeTableHtmlFile)

def _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=batchCodeTableHtmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                BatchcodeOptionsSetter().setBatchcodeOptions(
                    html=str(soup),
                    options=batchcodeOptions),
                'lxml'))

def saveLastUpdated2HtmlFile(lastUpdated, htmlFile):
    def setLastUpdated(soup):
        soup.find(id="last_updated").string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = htmlFile,
        soupTransformer = setLastUpdated)
