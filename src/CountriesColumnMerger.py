from CountriesMerger import CountriesMerger

class CountriesColumnMerger:

    @staticmethod
    def mergeCountriesColumnOfSrcIntoCountriesColumnOfDst(src, dst):
        COUNTRIES = 'Countries'
        dst[COUNTRIES] = CountriesMerger.mergeSrcIntoDst(
            dst = dst[COUNTRIES],
            src = src[COUNTRIES])
