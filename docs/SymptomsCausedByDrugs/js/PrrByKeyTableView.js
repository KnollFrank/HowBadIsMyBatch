class PrrByKeyTableView {

    #prrByKeyTable;
    #downloadPrrByKeyTableButton;
    #text;
    #valueName;
    #prrByKeyProvider;

    constructor(prrByKeyTable, downloadPrrByKeyTableButton, valueName, prrByKeyProvider) {
        this.#prrByKeyTable = prrByKeyTable;
        this.#prrByKeyTable.initialize();
        this.#initializeButton(downloadPrrByKeyTableButton);
        this.#valueName = valueName;
        this.#prrByKeyProvider = prrByKeyProvider;
    }

    displayPrrByKeyTable4Value(id, text) {
        UIUtils.disableButton(this.#downloadPrrByKeyTableButton);
        this.#prrByKeyProvider(id)
            .then(prrByKey => {
                this.#text = text;
                this.#prrByKeyTable.display(prrByKey);
                UIUtils.enableButton(this.#downloadPrrByKeyTableButton);
            });
    }

    getTable() {
        return this.#prrByKeyTable.getTable();
    }

    #initializeButton(downloadPrrByKeyTableButton) {
        this.#downloadPrrByKeyTableButton = downloadPrrByKeyTableButton;
        UIUtils.disableButton(downloadPrrByKeyTableButton);
        downloadPrrByKeyTableButton.addEventListener(
            'click',
            () => this.#downloadPrrByKey())
    }

    #downloadPrrByKey() {
        UrlUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [this.#prrByKeyTable.getDisplayedTableAsCsv(`# ${this.#valueName}: ${this.#text}`)],
                    { type: 'text/csv' })),
            this.#text);
    }
}
