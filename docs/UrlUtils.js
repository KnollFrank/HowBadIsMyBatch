class UrlUtils {

    static isSearchParamYES(urlParams, urlSearchParam) {
        return UrlUtils.#getSearchParam(urlParams, urlSearchParam, 'NO').toUpperCase() == 'YES';
    }

    static getSearchParamOfCurrentUrl(urlSearchParam) {
        return UrlUtils.#getSearchParam(
            new URLSearchParams(window.location.search), 
            urlSearchParam, 
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

    static #getSearchParam(urlParams, urlSearchParam, defaultValue) {
        return urlParams.has(urlSearchParam) ?
            urlParams.get(urlSearchParam) :
            defaultValue;
    }

    static #setSearchParam(url, nameOfSearchParam, valueOfSearchParam) {
        url.searchParams.set(nameOfSearchParam, valueOfSearchParam);
        window.history.replaceState(null, "", url);
    }
}
