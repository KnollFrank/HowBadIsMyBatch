class PageInitializer {

    static initializePage({ pathologySelectElement, drugsChartViewElement, urlSearchParam }) {
        PageInitializer.#configurePathologySelect(
            {
                pathologySelectElement: pathologySelectElement,
                drugsChartView: new DrugsChartView(drugsChartViewElement),
                urlSearchParam: urlSearchParam
            });
    }

    static #configurePathologySelect({ pathologySelectElement, drugsChartView, urlSearchParam }) {
        Select2.initializeSelectElement(
            {
                selectElement: pathologySelectElement,
                minimumInputLength: 0,
                textOfOption2Select: urlSearchParam.get(),
                onSelectOptionHavingValueAndText: (id, text) => {
                    PageInitializer
                        .#loadDrugDescr(id)
                        .then(drugDescr => {
                            drugsChartView.displayChart(drugDescr);
                            urlSearchParam.set(text);
                        });
                }
            });
    }

    static #loadDrugDescr(id) {
        return fetch(`data/DrugDescriptionsForPathologies/${id}.json`).then(response => response.json());
    }
}
