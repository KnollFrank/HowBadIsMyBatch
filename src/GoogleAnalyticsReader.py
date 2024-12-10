import linecache
import glob
from datetime import datetime


class GoogleAnalyticsReader:

    @staticmethod
    def getDateRange(dataDir):
        return GoogleAnalyticsReader._getMinMaxDateRange(GoogleAnalyticsReader._getDateRanges(dataDir))

    @staticmethod
    def _getDateRanges(dataDir):
        return [GoogleAnalyticsReader._getDateRange(file) for file in GoogleAnalyticsReader._getFiles(dataDir)]

    @staticmethod
    def _getFiles(dataDir):
        return glob.glob(dataDir + '/*')

    @staticmethod
    def _getDateRange(file):
        dateRangeLine = linecache.getline(file, 4)
        startDate, endDate = dateRangeLine[2:10], dateRangeLine[11:19]
        return GoogleAnalyticsReader._str2Date(startDate), GoogleAnalyticsReader._str2Date(endDate)

    @staticmethod
    def _str2Date(str):
        return datetime.strptime(str, '%Y%m%d').date()
    
    @staticmethod
    def _getMinMaxDateRange(dateRanges):
        minStartDate = min([GoogleAnalyticsReader._getStartDate(dateRange) for dateRange in dateRanges])
        maxEndDate = max([GoogleAnalyticsReader._getEndDate(dateRange) for dateRange in dateRanges])
        return minStartDate, maxEndDate
    
    @staticmethod
    def _getStartDate(dateRange):
        return dateRange[0]

    @staticmethod
    def _getEndDate(dateRange):
        return dateRange[1]
