class PrrByKeyTableView {

    #prrByKeyTable;
    #prrByKeyProvider;

    constructor(prrByKeyTable, prrByKeyProvider) {
        this.#prrByKeyTable = prrByKeyTable;
        this.#prrByKeyTable.initialize();
        this.#prrByKeyProvider = prrByKeyProvider;
    }

    displayPrrByKeyTable4Value(id) {
        this.#prrByKeyProvider(id)
            .then(prrByKey => this.#prrByKeyTable.display(prrByKey));
    }

    getTable() {
        return this.#prrByKeyTable.getTable();
    }
}
