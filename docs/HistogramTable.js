class HistogramTable {

    #tableElement;
    #table;

    constructor(tableElement) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
    }

    display(frequencyBySymptom) {
        const symptom_frequency_arrays = Object.entries(frequencyBySymptom);
        this.#setTableRows(symptom_frequency_arrays);
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

    #setTableRows(rows) {
        this.#table
            .clear()
            .rows.add(rows)
            .draw();
    }
}
