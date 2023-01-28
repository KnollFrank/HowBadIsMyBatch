class HistogramView {

    constructor() {
    }

    show(batchcode, uiContainer) {
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(json => {
                const data = json.histograms[3].histogram;
                const canvas = document.createElement("canvas");
                uiContainer.appendChild(canvas);
                new Chart(
                    canvas,
                    {
                        type: 'bar',
                        data: {
                            datasets: [{
                                label: 'Acquisitions by year',
                                data: data
                            }]
                        }
                    }
                );
            });
    }
}