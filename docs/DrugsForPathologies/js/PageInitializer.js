class PageInitializer {

    static initializePage({ pathologySelectElement, drugsChartViewElement, urlSearchParam }) {
        PageInitializer.#configurePathologySelect(pathologySelectElement, drugsChartViewElement, urlSearchParam);
    }

    static #configurePathologySelect(pathologySelectElement, drugsChartViewElement, urlSearchParam) {
        const drugsChartView = new DrugsChartView(drugsChartViewElement);
        Select2.initializeSelectElement(
            {
                selectElement: pathologySelectElement,
                minimumInputLength: 0,
                textOfOption2Select: urlSearchParam.get(),
                onSelectOptionHavingValueAndText: (id, text) => {
                    fetch(`data/DrugDescriptionsForPathologies/${id}.json`)
                        .then(response => response.json())
                        .then(drugDescr => {
                            drugsChartView.displayChart(drugDescr);
                            urlSearchParam.set(text);
                        });
                }
            });
    }
}
