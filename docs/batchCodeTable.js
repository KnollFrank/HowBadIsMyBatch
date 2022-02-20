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
    }

    #createEmptyBatchCodeTable() {
        const columnIndex = {
            'Batch': 0,
            'Adverse Reaction Reports': 1,
            'Deaths': 2,
            'Disabilities': 3,
            'Life Threatening Illnesses': 4,
            'Company': 5,
            'Severe reports': 6,
            'Lethality': 7
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
                            searchable: false,
                            targets: [
                                columnIndex['Adverse Reaction Reports'],
                                columnIndex['Deaths'],
                                columnIndex['Disabilities'],
                                columnIndex['Life Threatening Illnesses'],
                                columnIndex['Company'],
                                columnIndex['Severe reports'],
                                columnIndex['Lethality']
                            ]
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
        this.#batchCodeTable.ajax.url(`data/${country}.json`).load();
        this.#selectInput();
    }

    #selectInput() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }
}
