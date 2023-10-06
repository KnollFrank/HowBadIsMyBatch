import linecache
from GoogleAnalytics.Resolution import Resolution

class ResolutionProvider:

    @staticmethod
    def getResolution(file):
        columns = linecache.getline(file, 7)
        return Resolution.CITY if 'City' in columns else Resolution.COUNTRY
