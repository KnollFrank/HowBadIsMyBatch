from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from BatchcodeOptionsSetter import BatchcodeOptionsSetter
from HtmlUtils import getBatchcodeOptions, getBatchcodes
from DateProvider import DateProvider


def updateBatchCodeTableHtmlFile(batchCodeTable, batchCodeTableHtmlFile):
    batchcodeOptions = getBatchcodeOptions(getBatchcodes(batchCodeTable.sort_values(by = 'Adverse Reaction Reports', ascending = False)))
    _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile)
    _saveLastUpdatedBatchCodeTable(
        DateProvider().getLastUpdatedDataSource(),
        batchCodeTableHtmlFile)

def _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=batchCodeTableHtmlFile,
        soupTransformer=lambda soup:
            BeautifulSoup(
                BatchcodeOptionsSetter().setBatchcodeOptions(
                    html=str(soup),
                    options=batchcodeOptions),
                'lxml'))

def _saveLastUpdatedBatchCodeTable(lastUpdated, batchCodeTableHtmlFile):
    def setLastUpdated(soup):
        soup.find(id="last_updated").string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file=batchCodeTableHtmlFile,
        soupTransformer=setLastUpdated)
