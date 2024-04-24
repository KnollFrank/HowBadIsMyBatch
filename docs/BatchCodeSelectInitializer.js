class BatchCodeSelectInitializer {

    static initialize({ batchCodeSelectElement, batchCodeDetailsElement, batchCodeHeadingElement }) {
        const batchCodeDetailsView = new BatchCodeDetailsView(batchCodeDetailsElement);
        batchCodeSelectElement.select2({ minimumInputLength: 4 });
        batchCodeSelectElement.on(
            'select2:select',
            function (event) {
                BatchCodeSelectInitializer.#onBatchCodeSelected(
                    {
                        batchcode: event.params.data.id,
                        batchCodeHeadingElement: batchCodeHeadingElement,
                        batchCodeDetailsView: batchCodeDetailsView
                    });
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
