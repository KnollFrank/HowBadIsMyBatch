class BatchcodeCombinationSelection {

    static configureSelectBatchcodeCombinationElement({ batchcodesSelectElement, histograms, onSelect }) {
        this.#setBatchcodeCombinationOptions(batchcodesSelectElement.element, histograms);
        batchcodesSelectElement.setSingleChangeEventListener(
            event => {
                const histoDescr = histograms[event.target.value];
                onSelect(histoDescr);
            });
        onSelect(histograms[0]);
    }

    static #setBatchcodeCombinationOptions(batchcodesSelectElement, histograms) {
        UIUtils.clear(batchcodesSelectElement);
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchcodesSelectElement.add(option));
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