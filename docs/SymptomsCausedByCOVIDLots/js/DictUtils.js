class DictUtils {

    static retainCommonKeys({ dict1, dict2 }) {
        const commonKeys = DictUtils.#getCommonKeys(dict1, dict2);
        return {
            dict1: DictUtils.#retainKeysOfDict(dict1, commonKeys),
            dict2: DictUtils.#retainKeysOfDict(dict2, commonKeys)
        };
    }

    static #getCommonKeys(dict1, dict2) {
        return Sets.intersection(
            DictUtils.#getKeySet(dict1),
            DictUtils.#getKeySet(dict2));
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