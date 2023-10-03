import glob
from GoogleAnalytics.ResolutionProvider import ResolutionProvider


class GoogleAnalyticsReader:

    def __init__(self, dataDir):
        self.dataDir = dataDir

    def getFilesHavingResolution(self, resolution):
        return [file for file in self._getFiles() if ResolutionProvider.getResolution(file) == resolution]

    def _getFiles(self):
        return glob.glob(self.dataDir + '/*')
