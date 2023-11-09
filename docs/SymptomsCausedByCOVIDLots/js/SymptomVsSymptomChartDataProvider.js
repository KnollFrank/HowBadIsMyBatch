class SymptomVsSymptomChartDataProvider {

    // FK-TODO: extract utility class and test
    static retainCommonKeys({ dict1, dict2 }) {
        const commonKeys = SymptomVsSymptomChartDataProvider.#getCommonKeys(dict1, dict2);
        return {
            dict1: SymptomVsSymptomChartDataProvider.#retainKeysOfDict(dict1, commonKeys),
            dict2: SymptomVsSymptomChartDataProvider.#retainKeysOfDict(dict2, commonKeys)
        };
    }

    static getChartData({ prrByLotX, prrByLotY }) {
        const { dict1: prrByLotXCommon, dict2: prrByLotYCommon } =
            SymptomVsSymptomChartDataProvider.retainCommonKeys(
                {
                    dict1: prrByLotX,
                    dict2: prrByLotY
                });
        const lots = Object.keys(prrByLotXCommon);
        return {
            labels: lots,
            data:
                lots.map(
                    lot => ({
                        x: prrByLotXCommon[lot],
                        y: prrByLotYCommon[lot]
                    }))
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