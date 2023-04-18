class HistogramTable {

    #tableElement;
    #table;
    #sumFrequencies;

    constructor(tableElement) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
    }

    display(frequencyBySymptom) {
        const symptom_frequency_pairs = Object.entries(frequencyBySymptom);
        this.#setTableRows(symptom_frequency_pairs);
    }

    #createEmptyTable() {
        return this.#tableElement.DataTable(
            {
                language:
                {
                    searchPlaceholder: "Enter Symptom"
                },
                search:
                {
                    return: false
                },
                processing: true,
                deferRender: true,
                order: [[this.#getColumnIndex('Frequency'), "desc"]],
                columnDefs:
                    [
                        {
                            searchable: true,
                            targets: [
                                this.#getColumnIndex('Symptom')
                            ]
                        },
                        {
                            render: frequency =>
                                NumberWithBarElementFactory
                                    .createNumberWithBarElement(
                                        {
                                            number: frequency,
                                            barLenInPercent: frequency / this.#sumFrequencies * 100
                                        })
                                    .outerHTML,
                            targets: [this.#getColumnIndex('Frequency')]
                        }
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'Symptom':
                return 0;
            case 'Frequency':
                return 1;
        }
    }

    #setTableRows(symptom_frequency_pairs) {
        this.#sumFrequencies = this.#getSumFrequencies(symptom_frequency_pairs);
        this.#table
            .clear()
            .rows.add(symptom_frequency_pairs)
            .draw();
    }

    #getSumFrequencies(symptom_frequency_pairs) {
        const frequencies = symptom_frequency_pairs.map(symptom_frequency_pair => symptom_frequency_pair[1])
        return Utils.sum(frequencies);
    }
}
