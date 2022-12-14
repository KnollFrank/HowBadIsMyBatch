from decouple import AutoConfig
from Datawrapper import Datawrapper
from ColumnsAdder import ColumnsAdder
from KreiseReader import readKreise
from MedianOfFreeBedsByKreisTableFactory import MedianOfFreeBedsByKreisTableFactory


def createMedianOfFreeBedsByKreisChart(timeSeries, chartTitle):
    dataWrapper = Datawrapper(AutoConfig(search_path='../..')('DATAWRAPPER_API_TOKEN'))
    dataWrapper.setChartTitle(chartTitle)
    dataWrapper.uploadChartData(data = _createMedianOfFreeBedsByKreisTableForChoroplethMap(timeSeries))
    dataWrapper.publishChart()

def _createMedianOfFreeBedsByKreisTableForChoroplethMap(timeSeries):
    medianOfFreeBedsByKreisTableFactory = MedianOfFreeBedsByKreisTableFactory(timeSeries)
    medianOfFreeBedsByKreisTable = medianOfFreeBedsByKreisTableFactory.createMedianOfFreeBedsByKreisTable('gemeindeschluessel').reset_index()
    return ColumnsAdder(readKreise()).addKreisAndEinwohnerzahlColumns(medianOfFreeBedsByKreisTable)
