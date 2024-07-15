class PdfCreator {

    static createPdf() {
        const documentDefinition = {
            content: [
                { text: 'EU Safety Signal (All drugs)', fontSize: 16, alignment: 'center', margin: [0, 0, 0, 20], bold: true },
                { text: 'Worst Drugs', fontSize: 12, alignment: 'left', margin: [0, 10, 0, 10], bold: true },
                { text: 'table' },
                { text: 'Strongest Symptoms', fontSize: 12, alignment: 'left', margin: [0, 10, 0, 10], bold: true },
                { text: 'table' },
            ]
        }
        return pdfMake.createPdf(documentDefinition);
        // pdfMake.createPdf(documentDefinition).download();
    }
}