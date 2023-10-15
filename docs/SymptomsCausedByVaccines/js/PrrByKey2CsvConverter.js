class PrrByKey2CsvConverter {

    static convertPrrByKey2Csv({ prrByKey, keyColumn, prrColumn }) {
        return PrrByKey2CsvConverter.#convert2Csv(
            {
                prrByKey: PrrByKey2CsvConverter.#quoteKeys(prrByKey),
                keyColumn: PrrByKey2CsvConverter.#quote(keyColumn),
                prrColumn: PrrByKey2CsvConverter.#quote(prrColumn)
            });
    }

    static #quoteKeys(prrByKey) {
        return Object.fromEntries(
            Object
                .entries(prrByKey)
                .map(([key, prr]) => [PrrByKey2CsvConverter.#quote(key), prr]))
    }

    static #quote(str) {
        return '"' + str + '"';
    }

    static #convert2Csv({ prrByKey, keyColumn, prrColumn }) {
        const header = `${keyColumn},${prrColumn}`;
        return `${header}\n${PrrByKey2CsvConverter.#convertDict2Csv(prrByKey)}`;
    }

    static #convertDict2Csv(dict) {
        return Object
            .entries(dict)
            .map(([key, value]) => `${key},${value}`)
            .join('\n');
    }
}
