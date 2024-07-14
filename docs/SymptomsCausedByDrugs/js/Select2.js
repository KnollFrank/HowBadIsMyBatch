class Select2 {

    static initializeSelectElement(
        {
            selectElement,
            textOfOption2Select,
            onSelectOptionHavingValueAndText,
            minimumInputLength
        }) {
        selectElement.select2({ minimumInputLength: minimumInputLength });
        selectElement.on(
            'select2:select',
            function (event) {
                const id = event.params.data.id;
                const text = event.params.data.text;
                onSelectOptionHavingValueAndText(id, text);
            });
        Select2.#selectOptionHavingText(selectElement, textOfOption2Select);
    }

    static #selectOptionHavingText(selectElement, text) {
        const option = Select2.#getOptionHavingText(selectElement, text);
        if (option === undefined) {
            return;
        }
        Select2.#selectOption(selectElement, option);
    }

    static #getOptionHavingText(selectElement, text) {
        if (text === null) {
            return undefined;
        }
        return Array
            .from(selectElement[0].options)
            .find(option => option.text == text);
    }

    static #selectOption(selectElement, option) {
        selectElement.val(option.value).trigger('change');
        selectElement.trigger({
            type: 'select2:select',
            params: {
                data: {
                    "id": option.value,
                    "text": option.text
                }
            }
        });
    }
}
