class PrrByKeyTableView {

    #prrByKeyTable;
    #prrByKeyProvider;

    // FK-TODO: remove downloadPrrByKeyTableButton and valueName
    constructor(prrByKeyTable, downloadPrrByKeyTableButton, valueName, prrByKeyProvider) {
        this.#prrByKeyTable = prrByKeyTable;
        this.#prrByKeyTable.initialize();
        this.#prrByKeyProvider = prrByKeyProvider;
    }

    displayPrrByKeyTable4Value(id, text) {
        this.#prrByKeyProvider(id)
            .then(prrByKey => this.#prrByKeyTable.display(prrByKey));
    }

    getTable() {
        return this.#prrByKeyTable.getTable();
    }
}
