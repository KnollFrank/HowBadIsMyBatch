import linecache
import glob
from datetime import datetime


class GoogleAnalyticsReader:

    def __init__(self, dataDir):
        self.dataDir = dataDir

    def getDateRange(self):
        return self._getMinMaxDateRange(self._getDateRanges())

    def _getDateRanges(self):
        return [self._getDateRange(file) for file in self._getFiles()]

    def _getFiles(self):
        return glob.glob(self.dataDir + '/*')

    def _getDateRange(self, file):
        dateRangeLine = linecache.getline(file, 4)
        startDate, endDate = dateRangeLine[2:10], dateRangeLine[11:19]
        return self._str2Date(startDate), self._str2Date(endDate)

    def _str2Date(self, str):
        return datetime.strptime(str, '%Y%m%d').date()
    
    def _getMinMaxDateRange(self, dateRanges):
        minStartDate = min([self._getStartDate(dateRange) for dateRange in dateRanges])
        maxEndDate = max([self._getEndDate(dateRange) for dateRange in dateRanges])
        return minStartDate, maxEndDate
    
    def _getStartDate(self, dateRange):
        return dateRange[0]

    def _getEndDate(self, dateRange):
        return dateRange[1]
