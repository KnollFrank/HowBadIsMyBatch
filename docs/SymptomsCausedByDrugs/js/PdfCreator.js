class PdfCreator {

    static createPdf({ symptom, vaccine }) {
        const documentDefinition = {
            content: [
                {
                    text: 'EU Safety Signal (All drugs)',
                    fontSize: 18,
                    alignment: 'center',
                    margin: [0, 0, 0, 20],
                    bold: true
                },
                ...PdfCreator.#getWorstDrugsSection(symptom),
                ...PdfCreator.#getStrongestSymptoms(vaccine)
            ]
        }
        return pdfMake.createPdf(documentDefinition);
    }

    static #getWorstDrugsSection({ selectElement, table }) {
        return [
            PdfCreator.#getHeading(`Worst Drugs for ${PdfCreator.#getSelection(selectElement)}`),
            PdfCreator.#getTable(table)
        ];
    }

    static #getStrongestSymptoms({ selectElement, table }) {
        return [
            PdfCreator.#getHeading(`Strongest Symptoms for ${PdfCreator.#getSelection(selectElement)}`),
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