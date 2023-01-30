class BatchCodeTableInitializer {

    #heading;
    #countrySelect;
    #batchCodeTableElement;
    #batchCodeTable;

    constructor({ heading, countrySelect, batchCodeTableElement }) {
        this.#heading = heading;
        this.#countrySelect = countrySelect;
        this.#batchCodeTableElement = batchCodeTableElement;
    }

    initialize() {
        this.#batchCodeTable = this.#createEmptyBatchCodeTable();
        this.#countrySelect.addEventListener('change', event => this.#displayCountry(event.target.value));
        this.#displayCountry('Global');
        this.#initializeHistogramView();
    }

    #createEmptyBatchCodeTable() {
        return this.#batchCodeTableElement.DataTable(
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
                order: [[this.#getColumnIndex('Adverse Reaction Reports'), "desc"]],
                columnDefs:
                    [
                        {
                            className: 'dt-control',
                            orderable: false,
                            data: null,
                            defaultContent: '',
                            targets: this.#getColumnIndex('control')
                        },
                        {
                            searchable: false,
                            targets: [
                                this.#getColumnIndex('Adverse Reaction Reports'),
                                this.#getColumnIndex('Deaths'),
                                this.#getColumnIndex('Disabilities'),
                                this.#getColumnIndex('Life Threatening Illnesses'),
                                this.#getColumnIndex('Company'),
                                this.#getColumnIndex('Countries'),
                                this.#getColumnIndex('Severe reports'),
                                this.#getColumnIndex('Lethality')
                            ]
                        },
                        {
                            orderable: false,
                            targets: this.#getColumnIndex('Countries')
                        },
                        {
                            render: (data, type, row) => {
                                const numberInPercent = parseFloat(data);
                                return !isNaN(numberInPercent) ? numberInPercent.toFixed(2) + " %" : '';
                            },
                            targets: [this.#getColumnIndex('Severe reports'), this.#getColumnIndex('Lethality')]
                        }
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'control':
                return 0;
            case 'Batch':
                return 1;
            case 'Adverse Reaction Reports':
                return 2;
            case 'Deaths':
                return 3;
            case 'Disabilities':
                return 4;
            case 'Life Threatening Illnesses':
                return 5;
            case 'Company':
                return 6;
            case 'Countries':
                return 7;
            case 'Severe reports':
                return 8;
            case 'Lethality':
                return 9;
        }
    }

    #displayCountry(country) {
        this.#heading.textContent = country == 'Global' ? 'Global Batch Codes' : `Batch Codes for ${country}`;
        fetch(`data/batchCodeTables/${country}.json`)
            .then(response => response.json())
            .then(json => {
                this.#_addEmptyControlColumn(json);
                return json;
            })
            .then(json => {
                this.#_setTableRows(json.data)
                this.#selectInput();
            });
    }

    #_addEmptyControlColumn(json) {
        json.columns.unshift('control');
        json.data.forEach(row => row.unshift(null));
    }

    #_setTableRows(rows) {
        this.#batchCodeTable
            .clear()
            .rows.add(rows)
            .draw();
    }

    #selectInput() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }

    #initializeHistogramView() {
        const thisClassInstance = this;
        $(`#${this.#batchCodeTableElement[0].id} tbody`).on(
            'click',
            'td.dt-control',
            function () {
                const tr = $(this).closest('tr');
                const row = thisClassInstance.#batchCodeTable.row(tr);
                if (row.child.isShown()) {
                    row.child.hide();
                    tr.removeClass('shown');
                } else {
                    const uiContainer = document.createElement("div");
                    row.child(uiContainer).show();
                    tr.addClass('shown');
                    const batchcode = row.data()[thisClassInstance.#getColumnIndex('Batch')];
                    new HistogramView(uiContainer).displayHistogramViewForBatchcode(batchcode);
                }
            });
    }
}
