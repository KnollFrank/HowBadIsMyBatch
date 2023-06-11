class VaccineDistributionByZipcodeTableInitializer {

    #tableElement;

    constructor({ tableElement }) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#createTable();
        DataTablesFilter.selectDataTablesFilter();
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
            case 'Doses Shipped':
                return 3;
            case 'Statistical Number of Adverse Reaction Reports':
                return 4;
            case 'Statistical Number of Adverse Reaction Reports (per 100,000)':
                return 5;
        }
    }
}
