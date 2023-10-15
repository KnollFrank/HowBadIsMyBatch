class Dict2CsvConverter {

    static convertDict2CSV(dict) {
        const { 'keys': columns, 'values': firstRow } = Utils.getKeysAlignedWithValues(dict);
        return `${Dict2CsvConverter.#quoteValues(columns)}\n${firstRow}`;
    }

    static #quoteValues(values) {
        return values.map(Dict2CsvConverter.#quoteValue);
    }

    static #quoteValue(value) {
        return '"' + value + '"';
    }
}
