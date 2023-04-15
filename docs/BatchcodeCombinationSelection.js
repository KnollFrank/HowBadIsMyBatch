class BatchcodeCombinationSelection {

    static configureSelectBatchcodeCombinationElement({ selectBatchcodeCombinationElement, histograms, onSelect }) {
        const batchcodesSelect = selectBatchcodeCombinationElement.querySelector('#batchcodesSelect');
        this.#setBatchcodeCombinationOptions(batchcodesSelect, histograms);
        batchcodesSelect.addEventListener(
            'change',
            event => {
                const histoDescr = histograms[event.target.value];
                onSelect(histoDescr);
            });
            onSelect(histograms[0]);
    }

    static #setBatchcodeCombinationOptions(batchcodesSelect, histograms) {
        UIUtils.clear(batchcodesSelect);
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchcodesSelect.add(option));
    }

    static #getBatchcodeCombinationOptions(histograms) {
        return histograms.map(this.#getBatchcodeCombinationOption);
    }

    static #getBatchcodeCombinationOption(histoDescr, index) {
        const option = document.createElement("option");
        option.text = histoDescr.batchcodes.join(', ');
        option.value = index;
        return option;
    }
}