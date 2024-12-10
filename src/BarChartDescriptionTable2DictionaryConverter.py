from GoogleAnalyticsReader import GoogleAnalyticsReader
from CountriesByBatchcodeProvider import getDateRangeOfVAERSReports


class BarChartDescriptionTable2DictionaryConverter:

    @staticmethod
    def convert2Dictionary(barChartDescriptionTable, internationalVaersCovid19):
        return {
            'date range guessed': BarChartDescriptionTable2DictionaryConverter.dateRange2Str(GoogleAnalyticsReader.getDateRange(dataDir='data/GoogleAnalytics')),
            'date range known': BarChartDescriptionTable2DictionaryConverter.dateRange2Str(getDateRangeOfVAERSReports(internationalVaersCovid19)),
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
        return date.strftime("%b %d, %Y")
