class BatchCodeSelectInitializer {

    static initialize({ batchCodeSelectElement, urlSearchParam, batchCodeDetailsElement, batchCodeHeadingElement }) {
        const batchCodeDetailsView = new BatchCodeDetailsView(batchCodeDetailsElement);
        Select2.initializeSelectElement(
            {
                selectElement: batchCodeSelectElement,
                minimumInputLength: 4,
                textOfOption2Select: urlSearchParam.get(),
                onSelectOptionHavingValueAndText: (id, text) => {
                    BatchCodeSelectInitializer.#onBatchCodeSelected(
                        {
                            batchcode: id,
                            batchCodeHeadingElement: batchCodeHeadingElement,
                            batchCodeDetailsView: batchCodeDetailsView
                        });
                    urlSearchParam.set(text);
                }
            });
        batchCodeSelectElement.select2('open');
    }

    static #onBatchCodeSelected({ batchcode, batchCodeHeadingElement, batchCodeDetailsView }) {
        CompanyByBatchcodeProvider
            .getCompany(batchcode)
            .then(company => {
                batchCodeHeadingElement.innerText = `Batch ${batchcode} (${company})`;
                batchCodeDetailsView.displayBatchCodeDetails(batchcode);
                GoogleAnalytics.click_batchcode(batchcode);
            });
    }
}
