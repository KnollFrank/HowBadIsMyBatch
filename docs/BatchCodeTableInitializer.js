class BatchCodeTableInitializer {

    #batchCodeTableElement;
    #batchCodeTable;
    #columnSearch;
    #barChartDescriptions;

    constructor(batchCodeTableElement) {
        this.#batchCodeTableElement = batchCodeTableElement;
    }

    initialize() {
        this.#batchCodeTable = this.#createEmptyBatchCodeTable();
        this.#columnSearch = new ColumnSearch(this.#batchCodeTable.column(this.#getColumnIndex('Company')));
        this.#displayCountry();
        BarChartDescriptionsProvider
            .getBarChartDescriptions()
            .then(barChartDescriptions => {
                this.#barChartDescriptions = barChartDescriptions;

            });
    }

    #createEmptyBatchCodeTable() {
        return this.#batchCodeTableElement.DataTable(
            {
                language:
                {
                    searchPlaceholder: "Enter Batch Code"
                },
                searching: true,
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
                            searchable: false,
                            targets: [
                                this.#getColumnIndex('Adverse Reaction Reports'),
                                this.#getColumnIndex('Deaths'),
                                this.#getColumnIndex('Disabilities'),
                                this.#getColumnIndex('Life Threatening Illnesses'),
                                this.#getColumnIndex('Severe reports'),
                                this.#getColumnIndex('Lethality')
                            ]
                        },
                        {
                            orderable: false,
                            targets:
                                [
                                    this.#getColumnIndex('Batch'),
                                    this.#getColumnIndex('Company'),
                                    this.#getColumnIndex('Countries')
                                ]
                        },
                        {
                            render: data => {
                                const numberInPercent = parseFloat(data);
                                return !isNaN(numberInPercent) ? numberInPercent.toFixed(2) + "%" : '';
                            },
                            targets: [this.#getColumnIndex('Severe reports'), this.#getColumnIndex('Lethality')]
                        },
                        {
                            width: "1000px",
                            render: function (data, type, row, meta) {
                                return null;
                            },
                            createdCell: (cell, cellData, row, rowIndex, colIndex) => {
                                const batchcode = row[this.#getColumnIndex('Batch')];
                                if (batchcode in this.#barChartDescriptions) {
                                    const barChartDescription = this.#barChartDescriptions[batchcode];
                                    barChartDescription['batchcode'] = batchcode;
                                    new BatchcodeByCountryBarChartView(cell).displayBatchcodeByCountryBarChart(barChartDescription);
                                }
                            },
                            className: "dt-head-center",
                            targets: [this.#getColumnIndex('Countries')]
                        }
                    ]
            });
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'Batch':
                return 0;
            case 'Adverse Reaction Reports':
                return 1;
            case 'Deaths':
                return 2;
            case 'Disabilities':
                return 3;
            case 'Life Threatening Illnesses':
                return 4;
            case 'Company':
                return 5;
            case 'Severe reports':
                return 6;
            case 'Lethality':
                return 7;
            case 'Countries':
                return 8;
        }
    }

    // FK-TODO: rename
    #displayCountry() {
        // FK-TODO: show "Loading.." message or spinning wheel.
        BarChartDescriptionsProvider
            .getBarChartDescriptions()
            .then(barChartDescriptions => {
                this.#barChartDescriptions = barChartDescriptions;
                fetch('data/batchCodeTables/Global.json')
                    .then(response => response.json())
                    .then(json => {
                        this.#_addCountriesColumn(json);
                        return json;
                    })
                    .then(json => {
                        this.#setTableRows(json.data);
                        this.#columnSearch.columnContentUpdated();
                    });
            })
    }

    #_addCountriesColumn(json) {
        json.columns.push('Countries');
        json.data.forEach(row => row.push(null));
    }

    #setTableRows(rows) {
        this.#batchCodeTable
            .clear()
            .rows.add(rows)
            .draw();
    }
}
