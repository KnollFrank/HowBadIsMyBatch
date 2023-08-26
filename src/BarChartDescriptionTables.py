import math

class BarChartDescriptionTables:

    @staticmethod
    def filterValidJensenShannonDistances(barChartDescriptionTable):
        return barChartDescriptionTable[barChartDescriptionTable.apply(BarChartDescriptionTables._isValidJensenShannonDistance, axis = 'columns')]

    @staticmethod
    def _isValidJensenShannonDistance(barChartDescription):
        jensenShannonDistance = barChartDescription['BAR_CHART_DESCRIPTION']['Jensen-Shannon distance']
        return not math.isnan(jensenShannonDistance)
