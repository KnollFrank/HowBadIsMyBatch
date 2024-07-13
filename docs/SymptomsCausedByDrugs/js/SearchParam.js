class SearchParam {

    #name;

    constructor(name) {
        this.#name = name;
    }

    get() {
        return UIUtils.getSearchParamOfCurrentUrl(this.#name);
    }

    set(value) {
        UIUtils.setSearchParamOfCurrentUrl(this.#name, value);
    }
}