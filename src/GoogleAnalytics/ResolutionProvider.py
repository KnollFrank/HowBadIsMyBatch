from enum import Enum
import linecache


class Resolution(Enum):
    CITY = 1
    COUNTRY = 2


class ResolutionProvider:

    @staticmethod
    def getResolution(file):
        columns = linecache.getline(file, 7)
        return Resolution.CITY if 'City' in columns else Resolution.COUNTRY
