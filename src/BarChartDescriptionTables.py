import math
import numpy as np


class BarChartDescriptionTables:

    @staticmethod
    def filterValidJensenShannonDistances(barChartDescriptionTable):
        return barChartDescriptionTable[barChartDescriptionTable.apply(BarChartDescriptionTables._isValidJensenShannonDistance, axis='columns')]

    @staticmethod
    def _isValidJensenShannonDistance(barChartDescription):
        jensenShannonDistance = barChartDescription['BAR_CHART_DESCRIPTION']['Jensen-Shannon distance']
        return not math.isnan(jensenShannonDistance)

    @staticmethod
    def filterHasMinSizeOfGuessedHistogram(barChartDescriptionTable, minSizeOfGuessedHistogram):
        return barChartDescriptionTable[
            barChartDescriptionTable.apply(
                lambda barChartDescription: BarChartDescriptionTables._hasMinSizeOfGuessedHistogram(
                    barChartDescription, minSizeOfGuessedHistogram),
                axis='columns')]

    @staticmethod
    def _hasMinSizeOfGuessedHistogram(barChartDescription, minSizeOfGuessedHistogram):
        sizeOfGuessedHistogram = sum(barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports guessed'])
        return sizeOfGuessedHistogram >= minSizeOfGuessedHistogram

    @staticmethod
    def filterHasCountryWithGuessedGreaterThanKnown(barChartDescriptionTable):
        return barChartDescriptionTable[barChartDescriptionTable.apply(BarChartDescriptionTables._hasCountryWithGuessedGreaterThanKnown, axis='columns')]

    @staticmethod
    def _hasCountryWithGuessedGreaterThanKnown(barChartDescription):
        guessedBarChart = barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports guessed']
        knownBarChart = barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports known']
        return np.any(np.asarray(guessedBarChart) > np.asarray(knownBarChart))
