from Datawrapper import Datawrapper
from ColumnsAdder import ColumnsAdder
from KreiseReader import readKreise
from MedianOfFreeBedsByKreisTableFactory import MedianOfFreeBedsByKreisTableFactory


def createMedianOfFreeBedsByKreisChart(timeSeries, chartTitle, accessToken):
    dataWrapper = Datawrapper(accessToken)
    dataWrapper.setChartTitle(chartTitle)
    dataWrapper.uploadChartData(data = _createMedianOfFreeBedsByKreisTableForChoroplethMap(timeSeries))
    publishChartResult = dataWrapper.publishChart()
    print('publishChart:', publishChartResult)

def _createMedianOfFreeBedsByKreisTableForChoroplethMap(timeSeries):
    medianOfFreeBedsByKreisTableFactory = MedianOfFreeBedsByKreisTableFactory(timeSeries)
    medianOfFreeBedsByKreisTable = medianOfFreeBedsByKreisTableFactory.createMedianOfFreeBedsByKreisTable('gemeindeschluessel').reset_index()
    return ColumnsAdder(readKreise()).addKreisAndEinwohnerzahlColumns(medianOfFreeBedsByKreisTable)
