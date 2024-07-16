class PdfCreator {

    static createPdf(pdf) {
        return pdfMake.createPdf(PdfCreator.#createDocumentDefinition(pdf));
    }

    static #createDocumentDefinition({ symptom, vaccine, heading, valueName }) {
        return {
            content: [
                PdfCreator.#getPageHeading(heading),
                ...PdfCreator.#getWorstDrugsSection(symptom, valueName),
                ...PdfCreator.#getStrongestSymptomsSection(vaccine)
            ]
        };
    }

    static #getPageHeading(heading) {
        return {
            text: heading,
            fontSize: 18,
            alignment: 'center',
            margin: [0, 0, 0, 20],
            bold: true
        };
    }

    static #getWorstDrugsSection({ selectElement, table }, valueName) {
        return [
            PdfCreator.#getHeading(`Worst ${valueName} for "${PdfCreator.#getSelection(selectElement)}"`),
            PdfCreator.#getTable(table, true)
        ];
    }

    static #getStrongestSymptomsSection({ selectElement, table }) {
        return [
            PdfCreator.#getHeading(`Strongest Symptoms for "${PdfCreator.#getSelection(selectElement)}"`),
            PdfCreator.#getTable(table, false)
        ];
    }

    static #getHeading(text) {
        return {
            text: text,
            fontSize: 14,
            alignment: 'left',
            margin: [0, 15, 0, 15],
            bold: true
        }
    }

    static #getSelection(selectElement) {
        return selectElement.select2('data')[0].text;
    }

    static #getTable(table, shallMarkRowsIfPrrTooHigh) {
        return {
            layout: 'lightHorizontalLines',
            table: {
                headerRows: 1,
                body: [
                    PdfCreator.#getTableHeaders(table),
                    ...PdfCreator.#getMarkedRows(table, shallMarkRowsIfPrrTooHigh)
                ]
            }
        };
    }

    static #getTableHeaders(table) {
        return table
            .columns()
            .header()
            .map(header => ({
                text: header.textContent,
                bold: true
            }))
            .toArray();
    }

    static #getMarkedRows(table, shallMarkRowsIfPrrTooHigh) {
        const rows = PdfCreator.#getRows(table);
        return shallMarkRowsIfPrrTooHigh ?
            PdfCreator.#markRowsIfPrrTooHigh(rows) :
            rows;
    }

    static #getRows(table) {
        return table
            .rows({ search: 'applied' })
            .data()
            .toArray();
    }

    static #markRowsIfPrrTooHigh(rows) {
        return rows.map(PdfCreator.#markRowIfPrrTooHigh);
    }

    static #markRowIfPrrTooHigh(row) {
        const prr = row[1];
        return [
            PdfCreator.#markValueIfPrrTooHigh({ value: row[0], prr: prr }),
            PdfCreator.#markValueIfPrrTooHigh({ value: row[1], prr: prr })
        ];
    }

    static #markValueIfPrrTooHigh({ value, prr }) {
        return prr >= 2.0 ? PdfCreator.#markValue(value) : value;
    }

    static #markValue(value) {
        return {
            text: value,
            fillColor: '#FF0000',
            fillOpacity: 0.1,
        };
    }
}