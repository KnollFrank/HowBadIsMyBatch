class CountryCountsByBatchcodeTable2BarChartDescriptionTableConverter:

    @staticmethod
    def convert2BarChartDescriptionTable(countryCountsByBatchcodeTable):
        return (countryCountsByBatchcodeTable
                .reset_index(level = 'COUNTRY')
                .rename(
                    columns =
                        {
                            'COUNTRY': 'countries',
                            'COUNTRY_COUNT_BY_VAX_LOT Clicked': 'frequencies guessed',
                            'COUNTRY_COUNT_BY_VAX_LOT Before Deletion': 'frequencies before deletion'
                        })
                .groupby('VAX_LOT')
                .apply(lambda countryCountsTable: countryCountsTable.to_dict('list'))
                .rename('BAR_CHART_DESCRIPTION')
                .to_frame())
