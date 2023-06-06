import pandas as pd

class CountryCountsByBatchcodeTable2JsonConverter:

    @staticmethod
    def convert2Json(countryCountsByBatchcodeTable):
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
                .rename('HISTOGRAM_DESCRIPTION')
                .to_frame())
