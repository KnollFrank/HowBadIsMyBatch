from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from CountryOptionsSetter import CountryOptionsSetter
from DateProvider import DateProvider
from HtmlUtils import getCountryOptions, getCountries
from DateProvider import DateProvider
from BatchCodeTablePersister import createAndSaveBatchCodeTables


def updateBatchCodeTableHtmlFile(internationalVaersCovid19, batchCodeTableHtmlFile):
    countryOptions = getCountryOptions(getCountries(internationalVaersCovid19))
    _saveCountryOptions(countryOptions, batchCodeTableHtmlFile)
    _saveLastUpdatedBatchCodeTable(DateProvider().getLastUpdatedDataSource(), batchCodeTableHtmlFile)
    createAndSaveBatchCodeTables(internationalVaersCovid19, minADRsForLethality=100)


def _saveCountryOptions(countryOptions, batchCodeTableHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file = batchCodeTableHtmlFile,
        soupTransformer =
            lambda soup:
                BeautifulSoup(
                    CountryOptionsSetter().setCountryOptions(html = str(soup), options = countryOptions),
                    'lxml'))


def _saveLastUpdatedBatchCodeTable(lastUpdated, batchCodeTableHtmlFile):
    def setLastUpdated(soup):
        soup.find(id = "last_updated").string.replace_with(lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = batchCodeTableHtmlFile,
        soupTransformer = setLastUpdated)
    