class ScatterChart2CsvConverter {

    static convertScatterChart2Csv({ symptomX, symptomY, batches, data }) {
        const header = `"Batch","PRR ratio of Batch for ${symptomX}","PRR ratio of Batch for ${symptomY}"`;
        return `${header}\n${ScatterChart2CsvConverter.#asCsv(batches, data)}`;
    }

    static #asCsv(batches, data) {
        return Utils
            .zip([batches, data])
            .map(([batch, { x, y }]) => `${ScatterChart2CsvConverter.#quote(batch)},${x},${y}`)
            .join('\n');
    }

    static #quote(str) {
        return '"' + str + '"';
    }
}
