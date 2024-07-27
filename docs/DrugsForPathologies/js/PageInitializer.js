class PageInitializer {

    static initializePage({ pathologySelectElement, drugsChartViewElement }) {
        PageInitializer.#configurePathologySelect(pathologySelectElement, drugsChartViewElement);
    }

    static #configurePathologySelect(pathologySelectElement, drugsChartViewElement) {
        const drugsChartView = new DrugsChartView(drugsChartViewElement);
        Select2.initializeSelectElement(
            {
                selectElement: pathologySelectElement,
                minimumInputLength: 0,
                textOfOption2Select: null,
                onSelectOptionHavingValueAndText: (id, text) => {
                    fetch(`data/DrugDescriptionsForPathologies/${id}.json`)
                        .then(response => response.json())
                        .then(drugDescr => drugsChartView.displayChart(drugDescr));
                }
            });
    }
}
