from scipy.spatial import distance


class JensenShannonDistanceColumnAdder:

    @staticmethod
    def addJensenShannonDistanceColumn(barChartDescriptionTable):
        barChartDescriptionTable['JENSEN_SHANNON_DISTANCE'] = (
            barChartDescriptionTable.apply(
                lambda barChartDescription: distance.jensenshannon(
                    barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports guessed'],
                    barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports known'],
                    base=2.0),
                axis = 'columns'))
        return barChartDescriptionTable
