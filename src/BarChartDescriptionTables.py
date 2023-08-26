import math
import numpy as np


class BarChartDescriptionTables:

    @staticmethod
    def filterValidJensenShannonDistances(barChartDescriptionTable):
        return BarChartDescriptionTables._filter(
            barChartDescriptionTable,
            BarChartDescriptionTables._isValidJensenShannonDistance)

    @staticmethod
    def _isValidJensenShannonDistance(barChartDescription):
        jensenShannonDistance = barChartDescription['Jensen-Shannon distance']
        return not math.isnan(jensenShannonDistance)

    @staticmethod
    def filterHasMinSizeOfGuessedHistogram(barChartDescriptionTable, minSizeOfGuessedHistogram):
        return BarChartDescriptionTables._filter(
            barChartDescriptionTable,
            lambda barChartDescription:
                BarChartDescriptionTables._hasMinSizeOfGuessedHistogram(barChartDescription, minSizeOfGuessedHistogram))

    @staticmethod
    def _hasMinSizeOfGuessedHistogram(barChartDescription, minSizeOfGuessedHistogram):
        sizeOfGuessedHistogram = sum(
            barChartDescription['Adverse Reaction Reports guessed'])
        return sizeOfGuessedHistogram >= minSizeOfGuessedHistogram

    @staticmethod
    def filterHasCountryWithGuessedGreaterThanKnown(barChartDescriptionTable):
        return BarChartDescriptionTables._filter(
            barChartDescriptionTable,
            BarChartDescriptionTables._hasCountryWithGuessedGreaterThanKnown)

    @staticmethod
    def _hasCountryWithGuessedGreaterThanKnown(barChartDescription):
        guessedBarChart = barChartDescription['Adverse Reaction Reports guessed']
        knownBarChart = barChartDescription['Adverse Reaction Reports known']
        return np.any(np.asarray(guessedBarChart) > np.asarray(knownBarChart))

    @staticmethod
    def _filter(barChartDescriptionTable, predicate):
        return barChartDescriptionTable[barChartDescriptionTable.apply(
            lambda barChartDescription: predicate(
                barChartDescription['BAR_CHART_DESCRIPTION']),
            axis='columns')]
