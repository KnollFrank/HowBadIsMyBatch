class SearchParam {

    #name;

    constructor(name) {
        this.#name = name;
    }

    get() {
        return UrlUtils.getSearchParamOfCurrentUrl(this.#name);
    }

    set(value) {
        UrlUtils.setSearchParamOfCurrentUrl(this.#name, value);
    }
}