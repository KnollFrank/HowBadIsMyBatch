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
}
