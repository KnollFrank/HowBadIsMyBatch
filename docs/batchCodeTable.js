class BatchCodeTableInitializer {

    #heading;
    #countrySelect;
    #batchCodeTableElement;
    #batchCodeTable;
    #columnSearch;

    constructor({ heading, countrySelect, batchCodeTableElement }) {
        this.#heading = heading;
        this.#countrySelect = countrySelect;
        this.#batchCodeTableElement = batchCodeTableElement;
    }

    initialize() {
        this.#batchCodeTable = this.#createEmptyBatchCodeTable();
        this.#columnSearch = new ColumnSearch(this.#batchCodeTable.column(this.#getColumnIndex('Company')));
        this.#countrySelect.addEventListener('change', event => this.#displayCountry());
        this.#displayCountry();
        this.#initializeHistogramView();
        this.#trackSearchWithGoogleAnalytics();
    }

    #getCountry() {
        return UIUtils.getSelectedOption(this.#countrySelect).value;
    }

    #createEmptyBatchCodeTable() {
        return this.#batchCodeTableElement.DataTable(
            {
                initComplete: function () {
                    $('.dataTables_filter').append(' (press return key)');
                },
                language:
                {
                    searchPlaceholder: "Enter Batch Code"
                },
                search:
                {
                    return: true
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
                                this.#getColumnIndex('Countries'),
                                this.#getColumnIndex('Severe reports'),
                                this.#getColumnIndex('Lethality')
                            ]
                        },
                        {
                            orderable: false,
                            targets: [this.#getColumnIndex('Countries'), this.#getColumnIndex('Company')]
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

    #displayCountry() {
        this.#heading.textContent = this.#getCountry() == 'Global' ? 'Global Batch Codes' : `Batch Codes for ${this.#getCountry()}`;
        // FK-TODO: show "Loading.." message or spinning wheel.
        fetch(`data/batchCodeTables/${this.#getCountry()}.json`)
            .then(response => response.json())
            .then(json => {
                this.#_addEmptyControlColumn(json);
                return json;
            })
            .then(json => {
                this.#setTableRows(json.data);
                this.#columnSearch.columnContentUpdated();
                this.#selectInput();
            });
        GoogleAnalytics.countrySelected(this.#getCountry());
    }

    #_addEmptyControlColumn(json) {
        json.columns.unshift('control');
        json.data.forEach(row => row.unshift(null));
    }

    #setTableRows(rows) {
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
        $(`#${this.#batchCodeTableElement[0].id} tbody`)
            .on(
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
                        new HistogramView(uiContainer).displayHistogramView(thisClassInstance.#getCountry(), batchcode);
                        GoogleAnalytics.click_batchcode(batchcode);
                    }
                });
    }

    #trackSearchWithGoogleAnalytics() {
        const thisClassInstance = this;
        $(`#${this.#batchCodeTableElement[0].id}`)
            .on(
                'search.dt',
                function () {
                    GoogleAnalytics.view_search_results(thisClassInstance.#batchCodeTable.search().toUpperCase());
                });
    }
}
