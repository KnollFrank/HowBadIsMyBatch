class UrlUtils {

    static isSearchParamYES(urlParams, searchParam) {
        return UrlUtils.#getSearchParam(urlParams, searchParam, 'NO').toUpperCase() == 'YES';
    }

    static getSearchParamOfCurrentUrl(searchParam) {
        return UrlUtils.#getSearchParam(
            new URLSearchParams(window.location.search), 
            searchParam, 
            null)
    }

    static setSearchParamOfCurrentUrl(nameOfSearchParam, valueOfSearchParam) {
        UrlUtils.#setSearchParam(
            new URL(window.location.href),
            nameOfSearchParam,
            valueOfSearchParam);
    }

    static downloadUrlAsFilename(url, filename) {
        const a = document.createElement('a');
        a.setAttribute('href', url);
        a.setAttribute('download', filename);
        a.click();
    }

    static #getSearchParam(urlParams, searchParam, defaultValue) {
        return urlParams.has(searchParam) ?
            urlParams.get(searchParam) :
            defaultValue;
    }

    static #setSearchParam(url, nameOfSearchParam, valueOfSearchParam) {
        url.searchParams.set(nameOfSearchParam, valueOfSearchParam);
        window.history.replaceState(null, "", url);
    }
}
