class PrrByVaccineTable {

    #tableElement;
    #table;
    #sumPrrs;
    #prrByVaccine;

    constructor(tableElement) {
        this.#tableElement = tableElement;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
    }

    display(prrByVaccine) {
        this.#prrByVaccine = prrByVaccine;
        const vaccine_prr_pairs = Object.entries(prrByVaccine);
        this.#setTableRows(vaccine_prr_pairs);
    }

    getDisplayedTableAsCsv(heading) {
        return PrrByKey2CsvConverter.convertPrrByKey2Csv(
            {
                heading: heading,
                columns: {
                    keyColumn: 'Vaccine',
                    prrColumn: 'Proportional Reporting Ratio'
                },
                prrByKey: this.#prrByVaccine
            });
    }

    #createEmptyTable() {
        return this.#tableElement.DataTable(
            {
                search:
                {
                    return: false
                },
                processing: true,
                deferRender: true,
                order: [[this.#getColumnIndex('Proportional Reporting Ratio'), "desc"]],
                columnDefs:
                    [
                        {
                            searchable: false,
                            targets: [this.#getColumnIndex('Proportional Reporting Ratio')]
                        },
                        {
                            render: prr =>
                                NumberWithBarElementFactory
                                    .createNumberWithBarElement(
                                        {
                                            number: prr,
                                            barLenInPercent: prr / this.#sumPrrs * 100
                                        })
                                    .outerHTML,
                            targets: [this.#getColumnIndex('Proportional Reporting Ratio')]
                        }
                    ],
                createdRow: (row, data) => {
                    this.#markRowIfPrrTooHigh(
                        {
                            prr: data[this.#getColumnIndex('Proportional Reporting Ratio')],
                            row: row
                        });
                }
            });
    }

    #markRowIfPrrTooHigh({ prr, row }) {
        if (prr > 1.0) {
            $(row).addClass('prrTooHigh');
        }
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case 'Vaccine':
                return 0;
            case 'Proportional Reporting Ratio':
                return 1;
        }
    }

    #setTableRows(vaccine_prr_pairs) {
        this.#sumPrrs = this.#getSumPrrs(vaccine_prr_pairs);
        this.#table
            .clear()
            .rows.add(vaccine_prr_pairs)
            .draw();
    }

    #getSumPrrs(vaccine_prr_pairs) {
        const prrs = vaccine_prr_pairs.map(vaccine_prr_pair => vaccine_prr_pair[1])
        return Utils.sum(prrs);
    }
}
