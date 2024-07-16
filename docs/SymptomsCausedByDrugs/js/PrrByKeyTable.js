class PrrByKeyTable {

    #tableElement;
    #table;
    #sumPrrs;
    #prrByKey;
    #keyColumnName;
    #prrColumnName;
    #shallMarkRowIfPrrTooHigh;

    constructor({ tableElement, keyColumnName, prrColumnName, shallMarkRowIfPrrTooHigh }) {
        this.#tableElement = tableElement;
        this.#keyColumnName = keyColumnName;
        this.#prrColumnName = prrColumnName;
        this.#shallMarkRowIfPrrTooHigh = shallMarkRowIfPrrTooHigh;
    }

    initialize() {
        this.#table = this.#createEmptyTable();
    }

    display(prrByKey) {
        this.#prrByKey = prrByKey;
        const key_prr_pairs = Object.entries(prrByKey);
        this.#setTableRows(key_prr_pairs);
    }

    getDisplayedTableAsCsv(heading) {
        return PrrByKey2CsvConverter.convertPrrByKey2Csv(
            {
                heading: heading,
                columns: {
                    keyColumn: this.#keyColumnName,
                    prrColumn: this.#prrColumnName
                },
                prrByKey: this.#prrByKey
            });
    }

    getTable() {
        return this.#table;
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
                order: [[this.#getColumnIndex(this.#prrColumnName), "desc"]],
                columnDefs:
                    [
                        {
                            searchable: false,
                            targets: [this.#getColumnIndex(this.#prrColumnName)]
                        },
                        {
                            render: (prr, type, row, meta) =>
                                (type === 'sort' || type === 'type') ?
                                    parseFloat(prr) :
                                    NumberWithBarElementFactory
                                        .createNumberWithBarElement(
                                            {
                                                number: prr,
                                                barLenInPercent: prr / this.#sumPrrs * 100
                                            })
                                        .outerHTML,
                            targets: [this.#getColumnIndex(this.#prrColumnName)]
                        }
                    ],
                createdRow: (row, data) => {
                    if (this.#shallMarkRowIfPrrTooHigh) {
                        this.#markRowIfPrrTooHigh(
                            {
                                prr: data[this.#getColumnIndex(this.#prrColumnName)],
                                row: row
                            });
                    }
                }
            });
    }

    #markRowIfPrrTooHigh({ prr, row }) {
        if (prr >= 2.0) {
            $(row).addClass('prrTooHigh');
        }
    }

    #getColumnIndex(columnName) {
        switch (columnName) {
            case this.#keyColumnName:
                return 0;
            case this.#prrColumnName:
                return 1;
        }
    }

    #setTableRows(key_prr_pairs) {
        this.#sumPrrs = this.#getSumPrrs(key_prr_pairs);
        this.#table
            .clear()
            .rows.add(key_prr_pairs)
            .draw();
    }

    #getSumPrrs(key_prr_pairs) {
        const prrs = key_prr_pairs.map(key_prr_pair => key_prr_pair[1])
        return Utils.sum(prrs);
    }
}
