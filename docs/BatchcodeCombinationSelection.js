class BatchcodeCombinationSelection {

    getSelectBatchcodeCombination({ histograms, onSelect }) {
        const selectBatchcodeCombination = UIUtils.instantiateTemplate('template-selectBatchcodeCombination');
        const batchcodesSelect = selectBatchcodeCombination.querySelector('#batchcodesSelect');
        this.#addBatchcodeCombinationOptions(batchcodesSelect, histograms);
        batchcodesSelect.addEventListener(
            'change',
            event => {
                const histoDescr = histograms[event.target.value];
                onSelect(histoDescr);
            });
        return selectBatchcodeCombination;
    }

    #addBatchcodeCombinationOptions(batchcodesSelect, histograms) {
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchcodesSelect.add(option));
    }

    #getBatchcodeCombinationOptions(histograms) {
        return histograms.map(this.#getBatchcodeCombinationOption);
    }

    #getBatchcodeCombinationOption(histoDescr, index) {
        const option = document.createElement("option");
        option.text = histoDescr.batchcodes.join(', ');
        option.value = index;
        return option;
    }
}