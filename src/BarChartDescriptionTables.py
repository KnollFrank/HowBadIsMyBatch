import math
import numpy as np


class BarChartDescriptionTables:

    @staticmethod
    def filter(barChartDescriptionTable, predicate):
        return barChartDescriptionTable[barChartDescriptionTable.apply(
            lambda barChartDescription: predicate(
                barChartDescription['BAR_CHART_DESCRIPTION']),
            axis='columns')]

    @staticmethod
    def isValidJensenShannonDistance(barChartDescription):
        jensenShannonDistance = barChartDescription['Jensen-Shannon distance']
        return not math.isnan(jensenShannonDistance)

    @staticmethod
    def hasMinSizeOfGuessedHistogram(barChartDescription, minSizeOfGuessedHistogram):
        sizeOfGuessedHistogram = sum(
            barChartDescription['Adverse Reaction Reports guessed'])
        return sizeOfGuessedHistogram >= minSizeOfGuessedHistogram

    @staticmethod
    def hasMinSizeOfKnownHistogram(barChartDescription, minSizeOfKnownHistogram):
        sizeOfKnownHistogram = sum(
            barChartDescription['Adverse Reaction Reports known'])
        return sizeOfKnownHistogram >= minSizeOfKnownHistogram

    @staticmethod
    def hasCountryWithGuessedGreaterThanKnown(barChartDescription):
        guessedBarChart = barChartDescription['Adverse Reaction Reports guessed']
        knownBarChart = barChartDescription['Adverse Reaction Reports known']
        return np.any(np.asarray(guessedBarChart) > np.asarray(knownBarChart))

    @staticmethod
    def isGuessedGreaterThanKnown(barChartDescription):
        sizeOfGuessedHistogram = sum(
            barChartDescription['Adverse Reaction Reports guessed'])
        sizeOfKnownHistogram = sum(
            barChartDescription['Adverse Reaction Reports known'])
        return sizeOfGuessedHistogram >= sizeOfKnownHistogram

    @staticmethod
    def containsCountry(barChartDescription, country):
        COUNTRIES = [country.upper() for country in barChartDescription['countries']]
        return country.upper() in COUNTRIES
