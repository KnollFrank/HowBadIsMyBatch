from SymptomsCausedByVaccines.MultiLineFitting.Utils import generatePairs

class SymptomCombinationsProvider:

    @staticmethod
    def generateSymptomCombinations(prrByLotAndSymptom, dataFramePredicate):
        symptomPairs = SymptomCombinationsProvider._generatePairs(prrByLotAndSymptom.columns)
        symptomCombinations = (SymptomCombinationsProvider._generateSymptomCombination(prrByLotAndSymptom, symptomX, symptomY) for (symptomY, symptomX) in symptomPairs)
        return SymptomCombinationsProvider._filter(symptomCombinations, dataFramePredicate)

    @staticmethod
    def _generatePairs(symptoms):
        return ((symptoms[i], symptoms[j]) for (i, j) in generatePairs(len(symptoms)))

    @staticmethod
    def _generateSymptomCombination(prrByLotAndSymptom, symptomX, symptomY):
        df = prrByLotAndSymptom[[symptomX, symptomY]]
        return df[(df[symptomX] != 0) & (df[symptomY] != 0)]

    @staticmethod
    def _filter(dataFrames, dataFramePredicate):
        return (dataFrame for dataFrame in dataFrames if dataFramePredicate(dataFrame))
