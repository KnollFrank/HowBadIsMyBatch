from CountriesMerger import CountriesMerger

class CountriesColumnMerger:

    @staticmethod
    def mergeCountriesColumnOfSrcIntoCountriesColumnOfDst(src, dst):
        COUNTRIES = 'Countries'
        dst[COUNTRIES] = CountriesMerger.mergeSrcIntoDst(
            dst = dst[COUNTRIES],
            src = src[COUNTRIES])

    @staticmethod
    def mergeCountriesColumnOfSrcsIntoCountriesColumnOfDst(srcs, dst):
        for src in srcs:
            CountriesColumnMerger.mergeCountriesColumnOfSrcIntoCountriesColumnOfDst(src = src, dst = dst)
