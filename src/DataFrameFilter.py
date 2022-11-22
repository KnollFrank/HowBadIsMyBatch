import pandas as pd

class DataFrameFilter:
    
    def filterByCovid19(self, dataFrame):
        return dataFrame[self._isCovid19(dataFrame)]

    def _isCovid19(self, dataFrame):
        return dataFrame["VAX_TYPE"] == "COVID19"
