class VaccineDistributionByZipcodeTableInitializer {

    #tableElement;
    #table;

    constructor({ tableElement }) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
        this.#loadDataIntoTable();
    }

    #createEmptyTable() {
        return this.#tableElement.DataTable(
            {
                language:
                {
                    searchPlaceholder: "Enter Batch Code"
                },
                search:
                {
                    return: false
                },
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

    #loadDataIntoTable() {
        // FK-TODO: show "Loading.." message or spinning wheel.
        fetch('data/vaccineDistributionByZipcode/VaccineDistributionByZipcode.json')
            .then(response => response.json())
            .then(json => {
                this.#setTableRows(json.data);
                this.#selectInput();
            });
    }

    #setTableRows(rows) {
        this.#table
            .clear()
            .rows.add(rows)
            .draw();
    }

    #selectInput() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }
}
