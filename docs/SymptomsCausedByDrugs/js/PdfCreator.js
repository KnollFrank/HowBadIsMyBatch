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
            PdfCreator.#getTable(table)
        ];
    }

    static #getStrongestSymptomsSection({ selectElement, table }) {
        return [
            PdfCreator.#getHeading(`Strongest Symptoms for "${PdfCreator.#getSelection(selectElement)}"`),
            PdfCreator.#getTable(table)
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

    // FK-TODO: add red background to some rows
    static #getTable(table) {
        const headers = PdfCreator.#getTableHeaders(table);
        const rows = table.rows({ search: 'applied' }).data().toArray();
        return {
            layout: 'lightHorizontalLines',
            table: {
                headerRows: 1,
                body: [
                    headers,
                    ...rows
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
}