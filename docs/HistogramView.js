class HistogramView {

    constructor() {
    }

    show(batchcode, uiContainer) {
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescr => {
                const canvas = document.createElement("canvas");
                uiContainer.appendChild(canvas);
                this.#displayChart(histoDescr, canvas);
            });
    }

    #displayChart(histoDescr, canvas) {
        // FK-TODO: brauchen Slider wie bei intensivstationen
        new Chart(
            canvas,
            {
                type: 'bar',
                data: {
                    datasets: [{
                        label: histoDescr.batchcode,
                        data: histoDescr.histograms[0].histogram
                    }]
                }
            }
        );
    }
}