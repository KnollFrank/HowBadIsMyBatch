from scipy.spatial import distance


class JensenShannonDistance2BarChartDescriptionColumnAdder:

    @staticmethod
    def addJensenShannonDistance2BarChartDescriptionColumn(barChartDescriptionTable):
        barChartDescriptionTable['BAR_CHART_DESCRIPTION'] = (
            barChartDescriptionTable.apply(
                lambda barChartDescription:
                    {
                        **barChartDescription['BAR_CHART_DESCRIPTION'],
                        'Jensen-Shannon distance': distance.jensenshannon(
                            barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports guessed'],
                            barChartDescription['BAR_CHART_DESCRIPTION']['Adverse Reaction Reports known'],
                            base=2.0)
                    },
                axis='columns'))
        return barChartDescriptionTable
