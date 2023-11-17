import numpy as np

class CharacteristicFunctions:

    @staticmethod
    def apply(characteristicFunction, elements):
        return np.array(elements)[CharacteristicFunctions._getIndexes(characteristicFunction)]

    @staticmethod
    def _getIndexes(characteristicFunction):
        return [index for (index, value) in enumerate(characteristicFunction) if value == 1]
