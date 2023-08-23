from scipy.spatial import distance


class JensenShannonDistance2BarChartDescriptionColumnAdder:

    @staticmethod
    def addJensenShannonDistance2BarChartDescriptionColumn(barChartDescriptionTable):
        barChartDescriptionTable['BAR_CHART_DESCRIPTION'] = barChartDescriptionTable['BAR_CHART_DESCRIPTION'].map(
            JensenShannonDistance2BarChartDescriptionColumnAdder._addJensenShannonDistance2BarChartDescription)
        return barChartDescriptionTable

    @staticmethod
    def _addJensenShannonDistance2BarChartDescription(barChartDescription):
        return {
            **barChartDescription,
            # https://machinelearningmastery.com/divergence-between-probability-distributions/: 0 (identical) and 1 (maximally different)
            'Jensen-Shannon distance': distance.jensenshannon(
                barChartDescription['Adverse Reaction Reports guessed'],
                barChartDescription['Adverse Reaction Reports known'],
                base=2.0)
        }
