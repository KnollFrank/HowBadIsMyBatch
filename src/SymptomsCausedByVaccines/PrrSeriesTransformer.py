class PrrSeriesTransformer:

    @staticmethod
    def filterByNonZeroPrrs(prrByVaccineBySymptom):
        return PrrSeriesTransformer._filterPrrsBy(
            prrByVaccineBySymptom,
            lambda prr: prr != 0)

    @staticmethod
    def filterByHighPrrs(prrBySymptomByVaccine):
        return PrrSeriesTransformer._filterPrrsBy(
            prrBySymptomByVaccine,
            lambda prr: prr > 1)

    @staticmethod
    def _filterPrrsBy(prrByKeyByOtherKey, prrFilter):
        return prrByKeyByOtherKey.map(
            lambda prrByKey: {key: prr for key, prr in prrByKey.items() if prrFilter(prr)})
