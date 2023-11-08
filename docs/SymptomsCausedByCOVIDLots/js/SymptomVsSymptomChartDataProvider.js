class SymptomVsSymptomChartDataProvider {

    static retainCommonLots({ prrByLotX, prrByLotY }) {
        const commonLots = SymptomVsSymptomChartDataProvider.#getCommonKeys(prrByLotX, prrByLotY);
        return {
            prrByLotX: SymptomVsSymptomChartDataProvider.#retainKeysOfDict(prrByLotX, commonLots),
            prrByLotY: SymptomVsSymptomChartDataProvider.#retainKeysOfDict(prrByLotY, commonLots)
        };
    }

    static #getCommonKeys(dict1, dict2) {
        return Sets.intersection(
            SymptomVsSymptomChartDataProvider.#getKeySet(dict1),
            SymptomVsSymptomChartDataProvider.#getKeySet(dict2));
    }

    static #getKeySet(dict) {
        return new Set(Object.keys(dict));
    }

    static #retainKeysOfDict(dict, keys2Retain) {
        const entries2Retain =
            Object
                .entries(dict)
                .filter(([key, _]) => keys2Retain.has(key));
        return Object.fromEntries(entries2Retain);
    }
}