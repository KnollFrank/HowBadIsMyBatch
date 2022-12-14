from decouple import AutoConfig
from Datawrapper import Datawrapper

def createMedianOfFreeBedsByKreisChart(medianOfFreeBedsByKreisTable, chartTitle):
    config = AutoConfig(search_path='../..')
    dataWrapper = Datawrapper(config('DATAWRAPPER_API_TOKEN'))
    dataWrapper.setChartTitle(chartTitle)
    dataWrapper.uploadChartData(medianOfFreeBedsByKreisTable)
    dataWrapper.publishChart()
