class PrrByKeyTableView {

    #prrByKeyTable;
    #downloadPrrByKeyTableButton;
    #value;
    #valueName;
    #prrByKeyProvider;

    constructor(prrByKeyTable, downloadPrrByKeyTableButton, valueName, prrByKeyProvider) {
        this.#prrByKeyTable = prrByKeyTable;
        this.#prrByKeyTable.initialize();
        this.#initializeButton(downloadPrrByKeyTableButton);
        this.#valueName = valueName;
        this.#prrByKeyProvider = prrByKeyProvider;
    }

    displayPrrByKeyTable4Value(value) {
        UIUtils.disableButton(this.#downloadPrrByKeyTableButton);
        this.#prrByKeyProvider(value)
            .then(prrByKey => {
                this.#value = value;
                this.#prrByKeyTable.display(prrByKey);
                UIUtils.enableButton(this.#downloadPrrByKeyTableButton);
            });
    }

    #initializeButton(downloadPrrByKeyTableButton) {
        this.#downloadPrrByKeyTableButton = downloadPrrByKeyTableButton;
        UIUtils.disableButton(downloadPrrByKeyTableButton);
        downloadPrrByKeyTableButton.addEventListener(
            'click',
            () => this.#downloadPrrByKey())
    }

    #downloadPrrByKey() {
        UIUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [this.#prrByKeyTable.getDisplayedTableAsCsv(`# ${this.#valueName}: ${this.#value}`)],
                    { type: 'text/csv' })),
            this.#value
        );
    }
}
