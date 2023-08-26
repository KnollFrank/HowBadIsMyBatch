import math
import numpy as np


class BarChartDescriptionTables:

    @staticmethod
    def filterValidJensenShannonDistances(barChartDescriptionTable):
        return barChartDescriptionTable[barChartDescriptionTable.apply(
            lambda barChartDescription: BarChartDescriptionTables._isValidJensenShannonDistance(
                barChartDescription['BAR_CHART_DESCRIPTION']),
            axis='columns')]

    @staticmethod
    def _isValidJensenShannonDistance(barChartDescription):
        jensenShannonDistance = barChartDescription['Jensen-Shannon distance']
        return not math.isnan(jensenShannonDistance)

    @staticmethod
    def filterHasMinSizeOfGuessedHistogram(barChartDescriptionTable, minSizeOfGuessedHistogram):
        return barChartDescriptionTable[
            barChartDescriptionTable.apply(
                lambda barChartDescription: BarChartDescriptionTables._hasMinSizeOfGuessedHistogram(
                    barChartDescription['BAR_CHART_DESCRIPTION'], minSizeOfGuessedHistogram),
                axis='columns')]

    @staticmethod
    def _hasMinSizeOfGuessedHistogram(barChartDescription, minSizeOfGuessedHistogram):
        sizeOfGuessedHistogram = sum(
            barChartDescription['Adverse Reaction Reports guessed'])
        return sizeOfGuessedHistogram >= minSizeOfGuessedHistogram

    @staticmethod
    def filterHasCountryWithGuessedGreaterThanKnown(barChartDescriptionTable):
        return barChartDescriptionTable[barChartDescriptionTable.apply(
            lambda barChartDescription:BarChartDescriptionTables._hasCountryWithGuessedGreaterThanKnown(
                barChartDescription['BAR_CHART_DESCRIPTION']),
            axis='columns')]

    @staticmethod
    def _hasCountryWithGuessedGreaterThanKnown(barChartDescription):
        guessedBarChart = barChartDescription['Adverse Reaction Reports guessed']
        knownBarChart = barChartDescription['Adverse Reaction Reports known']
        return np.any(np.asarray(guessedBarChart) > np.asarray(knownBarChart))
