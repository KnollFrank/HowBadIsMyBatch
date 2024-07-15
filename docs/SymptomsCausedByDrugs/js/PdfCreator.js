class PdfCreator {

    static createPdf() {
        const documentDefinition = {
            content: [
                { text: 'Customizing Page Size and Orientation', fontSize: 16, bold: true },
                { text: 'This PDF has custom page size and orientation.' },
            ]
        }
        return pdfMake.createPdf(documentDefinition);
        // pdfMake.createPdf(documentDefinition).download();
    }
}