class PrrBySymptomTable {

    #tableElement;
    #table;
    #sumPrrs;

    constructor(tableElement) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
    }

    display(prrBySymptom) {
        const symptom_prr_pairs = Object.entries(prrBySymptom);
        this.#setTableRows(symptom_prr_pairs);
    }

    #createEmptyTable() {
        return this.#tableElement.DataTable(
            {
                search:
                {
                    return: false
                },
                processing: true,
                deferRender: true,
                order: [[this.#getColumnIndex('Proportional Reporting Ratio > 1'), "desc"]],
                columnDefs:
                    [
                        {
                            searchable: false,
                            targets: [this.#getColumnIndex('Proportional Reporting Ratio > 1')]
                        },
                        {
                            render: prr =>
                                NumberWithBarElementFactory
                                    .createNumberWithBarElement(
                                        {
                                            number: prr,
                                            barLenInPercent: prr / this.#sumPrrs * 100
                                        })
                                    .outerHTML,
                            targets: [this.#getColumnIndex('Proportional Reporting Ratio > 1')]
                        }
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'Symptom':
                return 0;
            case 'Proportional Reporting Ratio > 1':
                return 1;
        }
    }

    #setTableRows(symptom_prr_pairs) {
        this.#sumPrrs = this.#getSumPrrs(symptom_prr_pairs);
        this.#table
            .clear()
            .rows.add(symptom_prr_pairs)
            .draw();
    }

    #getSumPrrs(symptom_prr_pairs) {
        const prrs = symptom_prr_pairs.map(symptom_prr_pair => symptom_prr_pair[1])
        return Utils.sum(prrs);
    }
}
