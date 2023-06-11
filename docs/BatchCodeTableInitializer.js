class BatchCodeTableInitializer {

    initialize({ batchCodeTableElement, showCountriesColumn }) {
        // FK-TODO: show "Loading.." message or spinning wheel.
        this.#loadBarChartDescriptions(showCountriesColumn)
            .then(barChartDescriptions => {
                const batchCodeTable = this.#createEmptyBatchCodeTable(batchCodeTableElement, showCountriesColumn, barChartDescriptions);
                this.#setVisibilityOfCountriesColumn(batchCodeTable, showCountriesColumn);
                fetch('data/batchCodeTables/Global.json')
                    .then(response => response.json())
                    .then(json => {
                        this.#addCountriesColumn(json);
                        return json;
                    })
                    .then(json => {
                        this.#setTableRows(batchCodeTable, json.data);
                        this.#makeCompanyColumnSearchable(batchCodeTable);
                    });
            });
    }

    #loadBarChartDescriptions(shallLoad) {
        return shallLoad ?
            fetch('data/barChartDescriptionTable.json').then(response => response.json()) :
            Promise.resolve({});
    }

    #createEmptyBatchCodeTable(batchCodeTableElement, showCountriesColumn, barChartDescriptions) {
        return batchCodeTableElement.DataTable(
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
                            targets: [
                                this.#getColumnIndex('Severe reports'),
                                this.#getColumnIndex('Lethality')
                            ]
                        },
                        {
                            width: "1000px",
                            render: function (data, type, row, meta) {
                                return null;
                            },
                            createdCell: (cell, cellData, row, rowIndex, colIndex) => {
                                if (showCountriesColumn) {
                                    this.#displayBatchcodeByCountryBarChart(
                                        row[this.#getColumnIndex('Batch')],
                                        barChartDescriptions,
                                        cell);
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

    #displayBatchcodeByCountryBarChart(batchcode, barChartDescriptions, uiContainer) {
        if (batchcode in barChartDescriptions.barChartDescriptions) {
            new BatchcodeByCountryBarChartView(uiContainer)
                .displayBatchcodeByCountryBarChart(this.#getBarChartDescription(barChartDescriptions, batchcode));
        }
    }

    #getBarChartDescription(barChartDescriptions, batchcode) {
        const barChartDescription = barChartDescriptions.barChartDescriptions[batchcode];
        barChartDescription.batchcode = batchcode;
        barChartDescription['dateRange guessed'] = barChartDescriptions['dateRange guessed'];
        barChartDescription['dateRange before deletion'] = barChartDescriptions['dateRange before deletion'];
        return barChartDescription;
    }

    #setVisibilityOfCountriesColumn(batchCodeTable, showCountriesColumn) {
        batchCodeTable
            .column(this.#getColumnIndex('Countries'))
            .visible(showCountriesColumn);
    }

    #addCountriesColumn(json) {
        json.columns.push('Countries');
        json.data.forEach(row => row.push(null));
    }

    #setTableRows(batchCodeTable, rows) {
        batchCodeTable
            .clear()
            .rows.add(rows)
            .draw();
    }

    #makeCompanyColumnSearchable(batchCodeTable) {
        const companyColumnSearch = new ColumnSearch(batchCodeTable.column(this.#getColumnIndex('Company')));
        companyColumnSearch.columnContentUpdated();
    }
}
