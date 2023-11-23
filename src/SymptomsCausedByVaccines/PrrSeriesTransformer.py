class PrrSeriesTransformer:

    @staticmethod
    def filterByNonZeroPrrs(prrByVaccineBySymptom):
        return PrrSeriesTransformer.filterPrrs(
            prrByVaccineBySymptom,
            lambda prr: prr != 0)

    @staticmethod
    def filterPrrs(prrByKeyByOtherKey, prrFilter):
        return prrByKeyByOtherKey.map(
            lambda prrByKey: {key: prr for key, prr in prrByKey.items() if prrFilter(prr)})
