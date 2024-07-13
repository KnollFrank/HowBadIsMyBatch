class UIUtils {

    static show(element) {
        element.style.display = "block";
    }

    static hide(element) {
        element.style.display = "none";
    }

    static disableButton(button) {
        button.disabled = true;
    }

    static enableButton(button) {
        button.disabled = false;
    }

    static instantiateTemplate(templateId) {
        return document.getElementById(templateId).content.firstElementChild.cloneNode(true);
    }

    static clear(container) {
        container.replaceChildren();
    }

    static getSelectedOption(selectElement) {
        return selectElement.options[selectElement.selectedIndex];
    }

    static getSearchParam(urlParams, searchParam, defaultValue) {
        return urlParams.has(searchParam) ?
            urlParams.get(searchParam) :
            defaultValue;
    }

    static isSearchParamYES(urlParams, searchParam) {
        return UIUtils.getSearchParam(urlParams, searchParam, 'NO').toUpperCase() == 'YES';
    }

    static getSearchParamOfCurrentUrl(searchParam) {
        const urlSearchParams = new URLSearchParams(window.location.search);
        return UIUtils.getSearchParam(urlSearchParams, searchParam, null)
    }

    static setSearchParamOfCurrentUrl(nameOfSearchParam, valueOfSearchParam) {
        const url = new URL(window.location.href);
        url.searchParams.set(nameOfSearchParam, valueOfSearchParam);
        window.history.replaceState(null, "", url);
    }

    static downloadUrlAsFilename(url, filename) {
        const a = document.createElement('a');
        a.setAttribute('href', url);
        a.setAttribute('download', filename);
        a.click();
    }
}
