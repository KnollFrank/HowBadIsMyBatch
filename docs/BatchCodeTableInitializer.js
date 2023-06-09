class BatchCodeTableInitializer {

    #batchCodeTableElement;
    #barChartDescriptions;

    constructor(batchCodeTableElement) {
        this.#batchCodeTableElement = batchCodeTableElement;
    }

    initialize() {
        const self = this;
        BarChartDescriptionsProvider
            .getBarChartDescriptions()
            .then(barChartDescriptions => {
                this.#barChartDescriptions = barChartDescriptions;
                this.#batchCodeTableElement.DataTable(
                    {
                        ajax: 'data/batchCodeTables/Global.json',
                        initComplete: function (settings) {
                            batchCodeTable = settings.oInstance.api();
                            const columnSearch = new ColumnSearch(batchCodeTable.column(self.#getColumnIndex('Company')));
                            columnSearch.columnContentUpdated();
                        },
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
}
