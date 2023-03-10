class VaccineDistributionByZipcodeTableInitializer {

    #tableElement;

    constructor({ tableElement }) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#createTable();
        this.#selectInput();
    }

    #createTable() {
        this.#tableElement.DataTable(
            {
                search:
                {
                    return: false
                },
                ajax: 'data/vaccineDistributionByZipcode/VaccineDistributionByZipcode.json',
                processing: true,
                deferRender: true,
                columnDefs:
                    [
                        {
                            searchable: false,
                            orderable: false,
                            targets: [this.#getColumnIndex('Summary')]
                        },
                        {
                            searchable: true,
                            targets: [
                                this.#getColumnIndex('Provider'),
                                this.#getColumnIndex('ZIP Code'),
                                this.#getColumnIndex('Lot Number'),
                            ]
                        },
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'Provider':
                return 0;
            case 'ZIP Code':
                return 1;
            case 'Lot Number':
                return 2;
            case 'Summary':
                return 3;
        }
    }

    #selectInput() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }
}
