class PrrByKeyTableView {

    #prrByKeyTable;
    #prrByKeyProvider;

    constructor(prrByKeyTable, prrByKeyProvider) {
        this.#prrByKeyTable = prrByKeyTable;
        this.#prrByKeyTable.initialize();
        this.#prrByKeyProvider = prrByKeyProvider;
    }

    // FK-TODO: remove parameter text
    displayPrrByKeyTable4Value(id, text) {
        this.#prrByKeyProvider(id)
            .then(prrByKey => this.#prrByKeyTable.display(prrByKey));
    }

    getTable() {
        return this.#prrByKeyTable.getTable();
    }
}
