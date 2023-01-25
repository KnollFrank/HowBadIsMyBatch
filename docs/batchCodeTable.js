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
        this.#displayCountry('Global')
        function format(d) {
            const div = document.createElement("div");
            const canvas = document.createElement("canvas");
            canvas.setAttribute("id", "acquisitions");
            div.appendChild(canvas);
            return div;
        }
        const thisClassInstance = this;
        $('#' + this.#batchCodeTableElement[0].id + ' tbody').on(
            'click',
            'td.dt-control',
            function () {
                const tr = $(this).closest('tr');
                const row = thisClassInstance.#batchCodeTable.row(tr);
                if (row.child.isShown()) {
                    row.child.hide();
                    tr.removeClass('shown');
                } else {
                    const div = format(row.data());
                    row.child(div).show();
                    new Chart(
                        div.querySelector('#acquisitions'),
                        {
                            type: 'bar',
                            data: {
                                datasets: [{
                                    label: 'Acquisitions by year',
                                    data: {
                                        "Circulatory collapse": 1,
                                        "Hyperhidrosis": 4
                                    }
                                }]
                            }
                        }
                    );
                    tr.addClass('shown');
                }
            });
    }

    #createEmptyBatchCodeTable() {
        const columnIndex = {
            'control': 0,
            'Batch': 1,
            'Adverse Reaction Reports': 2,
            'Deaths': 3,
            'Disabilities': 4,
            'Life Threatening Illnesses': 5,
            'Company': 6,
            'Countries': 7,
            'Severe reports': 8,
            'Lethality': 9
        };
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
                order: [[columnIndex['Adverse Reaction Reports'], "desc"]],
                columnDefs:
                    [
                        {
                            className: 'dt-control',
                            orderable: false,
                            data: null,
                            defaultContent: '',
                            targets: columnIndex['control']
                        },
                        {
                            searchable: false,
                            targets: [
                                columnIndex['Adverse Reaction Reports'],
                                columnIndex['Deaths'],
                                columnIndex['Disabilities'],
                                columnIndex['Life Threatening Illnesses'],
                                columnIndex['Company'],
                                columnIndex['Countries'],
                                columnIndex['Severe reports'],
                                columnIndex['Lethality']
                            ]
                        },
                        {
                            orderable: false,
                            targets: columnIndex['Countries']
                        },
                        {
                            render: (data, type, row) => {
                                const numberInPercent = parseFloat(data);
                                return !isNaN(numberInPercent) ? numberInPercent.toFixed(2) + " %" : '';
                            },
                            targets: [columnIndex['Severe reports'], columnIndex['Lethality']]
                        }
                    ]
            });
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
}
