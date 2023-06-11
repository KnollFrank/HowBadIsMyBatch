from GoogleAnalyticsReader import GoogleAnalyticsReader
from CountriesByBatchcodeProvider import getDateRangeOfVAERSReportsBeforeDeletionOfCountryCodes


class BarChartDescriptionTable2DictionaryConverter:

    @staticmethod
    def convert2Dictionary(barChartDescriptionTable):
        return {
            'dateRange guessed': BarChartDescriptionTable2DictionaryConverter.dateRange2Str(GoogleAnalyticsReader(dataDir='data/GoogleAnalytics').getDateRange()),
            'dateRange before deletion': BarChartDescriptionTable2DictionaryConverter.dateRange2Str(getDateRangeOfVAERSReportsBeforeDeletionOfCountryCodes()),
            'barChartDescriptions': barChartDescriptionTable['BAR_CHART_DESCRIPTION'].to_dict()
        }

    @staticmethod
    def dateRange2Str(dateRange):
        return {
            'start': BarChartDescriptionTable2DictionaryConverter._date2Str(dateRange[0]),
            'end': BarChartDescriptionTable2DictionaryConverter._date2Str(dateRange[1])
        }

    @staticmethod
    def _date2Str(date):
        return date.strftime("%d.%m.%Y")
