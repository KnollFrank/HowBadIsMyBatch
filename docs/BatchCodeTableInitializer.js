class BatchCodeTableInitializer {

    initialize({ batchCodeTableElement, showCountriesColumn, showDataTablesFilter }) {
        // FK-TODO: show "Loading.." message or spinning wheel.
        this.#loadBarChartDescriptions(showCountriesColumn)
            .then(barChartDescriptions => {
                const batchCodeTable = this.#createEmptyBatchCodeTable(batchCodeTableElement, showCountriesColumn, barChartDescriptions);
                this.#setVisibilityOfCountriesColumn(batchCodeTable, showCountriesColumn);
                this.#setDataTablesFilter(showDataTablesFilter);
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
                    return: false
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
                                this.#getColumnIndex('Life-Threatening Illnesses'),
                                this.#getColumnIndex('Hospitalizations'),
                                this.#getColumnIndex('Severe reports'),
                                this.#getColumnIndex('Lethality')
                            ]
                        },
                        {
                            orderable: false,
                            targets:
                                [
                                    this.#getColumnIndex('Batch'),
                                    this.#getColumnIndex('Company')
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
                            render: (data, type, row, meta) => {
                                if (type === 'sort') {
                                    return this.#getJensenShannonDistance(
                                        row[this.#getColumnIndex('Batch')],
                                        barChartDescriptions);
                                }
                                return data;
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
            case 'Life-Threatening Illnesses':
                return 4;
            case 'Hospitalizations':
                return 5;
            case 'Company':
                return 6;
            case 'Severe reports':
                return 7;
            case 'Lethality':
                return 8;
            case 'Countries':
                return 9;
        }
    }

    #getJensenShannonDistance(batchcode, barChartDescriptions) {
        const barChartDescription = this.#getBarChartDescription(barChartDescriptions, batchcode);
        const maximally_different = 1;
        if (barChartDescription === null) {
            return maximally_different;
        }
        const jensenShannonDistance = barChartDescription['Jensen-Shannon distance'];
        return jensenShannonDistance === null ? maximally_different : jensenShannonDistance;
    }

    #displayBatchcodeByCountryBarChart(batchcode, barChartDescriptions, uiContainer) {
        const barChartDescription = this.#getBarChartDescription(barChartDescriptions, batchcode);
        if (barChartDescription !== null) {
            new BatchcodeByCountryBarChartView(uiContainer).displayBatchcodeByCountryBarChart(barChartDescription);
        }
    }

    #getBarChartDescription(barChartDescriptions, batchcode) {
        if (!(batchcode in barChartDescriptions.barChartDescriptions)) {
            return null;
        }
        const barChartDescription = barChartDescriptions.barChartDescriptions[batchcode];
        barChartDescription.batchcode = batchcode;
        barChartDescription['date range guessed'] = barChartDescriptions['date range guessed'];
        barChartDescription['date range known'] = barChartDescriptions['date range known'];
        return barChartDescription;
    }

    #setVisibilityOfCountriesColumn(batchCodeTable, showCountriesColumn) {
        batchCodeTable
            .column(this.#getColumnIndex('Countries'))
            .visible(showCountriesColumn);
    }

    #setDataTablesFilter(isEnabled) {
        DataTablesFilter.setDataTablesFilter(
            isEnabled ?
                DataTablesFilter.FilterState.Enabled :
                DataTablesFilter.FilterState.Disabled);
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
