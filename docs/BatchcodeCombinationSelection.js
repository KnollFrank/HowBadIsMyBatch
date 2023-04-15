class BatchcodeCombinationSelection {

    static configureSelectBatchcodeCombinationElement({ batchCodesSelectElement, histograms, onSelect }) {
        this.#setBatchcodeCombinationOptions(batchCodesSelectElement.element, histograms);
        batchCodesSelectElement.setSingleChangeEventListener(
            event => {
                const histoDescr = histograms[event.target.value];
                onSelect(histoDescr);
            });
        onSelect(histograms[0]);
    }

    static #setBatchcodeCombinationOptions(batchCodesSelectElement, histograms) {
        UIUtils.clear(batchCodesSelectElement);
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchCodesSelectElement.add(option));
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