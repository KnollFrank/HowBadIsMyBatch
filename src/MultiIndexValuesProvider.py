class MultiIndexValuesProvider:

    @staticmethod
    def getValues(multiIndex):
        return set(MultiIndexValuesProvider._concat(MultiIndexValuesProvider._tuples2Lists(multiIndex.values)))
    
    @staticmethod
    def _tuples2Lists(tuples):
        return [list(tuple) for tuple in tuples]

    @staticmethod
    def _concat(lsts):
        return sum(lsts, [])