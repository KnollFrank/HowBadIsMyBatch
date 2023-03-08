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
                            targets: [this.#getColumnIndex('DOSES_SHIPPED')]
                        },
                        {
                            searchable: true,
                            targets: [
                                this.#getColumnIndex('PROVIDER_NAME'),
                                this.#getColumnIndex('ZIPCODE_SHP'),
                                this.#getColumnIndex('LOT_NUMBER'),
                            ]
                        },
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'PROVIDER_NAME':
                return 0;
            case 'ZIPCODE_SHP':
                return 1;
            case 'LOT_NUMBER':
                return 2;
            case 'DOSES_SHIPPED':
                return 3;
        }
    }

    #selectInput() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }
}
