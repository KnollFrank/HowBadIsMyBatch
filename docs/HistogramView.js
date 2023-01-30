class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramViewForBatchcode(batchcode) {
        this
            .#loadHistoDescrsForBatchcode(batchcode)
            .then(histoDescrs => this.#displayHistogramViewForHistoDescrs(histoDescrs));
    }

    #loadHistoDescrsForBatchcode(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        return fetch(`data/histograms/${batchcode}.json`)
            .then(response => {
                loadingText.remove();
                return response.json();
            })
    }

    #displayHistogramViewForHistoDescrs(histoDescrs) {
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const histogramChartView = new HistogramChartView(chartWithSlider.querySelector("canvas"));
        const selectBatchcodeCombination = this.#displaySelectBatchcodeCombination(histoDescrs.histograms, histogramChartView, chartWithSlider);
        this.#uiContainer.appendChild(chartWithSlider);
        this.#displayHistogram(
            this.#getSelectedHistoDescr(selectBatchcodeCombination, histoDescrs.histograms),
            histogramChartView,
            chartWithSlider);
    }

    #displaySelectBatchcodeCombination(histograms, histogramChartView, chartWithSlider) {
        const selectBatchcodeCombination = UIUtils.instantiateTemplate('template-selectBatchcodeCombination');
        const batchcodesSelect = selectBatchcodeCombination.querySelector('#batchcodesSelect');
        this.#addBatchcodeCombinationOptions(batchcodesSelect, histograms);
        batchcodesSelect.addEventListener(
            'change',
            event => {
                const histoDescr = histograms[event.target.value];
                this.#displayHistogram(histoDescr, histogramChartView, chartWithSlider);
            });
        this.#uiContainer.appendChild(selectBatchcodeCombination);
        return selectBatchcodeCombination;
    }

    #getSelectedHistoDescr(selectBatchcodeCombination, histograms) {
        const selectedIndex = UIUtils.getSelectedOption(selectBatchcodeCombination.querySelector('#batchcodesSelect')).value;
        return histograms[selectedIndex];
    }

    #addBatchcodeCombinationOptions(batchcodesSelect, histograms) {
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchcodesSelect.add(option));
    }

    #getBatchcodeCombinationOptions(histograms) {
        const options = histograms.map(this.#getBatchcodeCombinationOption);
        const mapped = histograms.map((histoDescr, index) => ({ index: index, value: histoDescr.batchcodes.length }));
        mapped.sort((a, b) => {
            if (a.value > b.value) {
                return 1;
            }
            if (a.value < b.value) {
                return -1;
            }
            return 0;
        });
        const optionsSorted = mapped.map(v => options[v.index]);
        optionsSorted[0].selected = true;
        return optionsSorted;
    }

    #getBatchcodeCombinationOption(histoDescr, index) {
        const option = document.createElement("option");
        option.text = histoDescr.batchcodes.join(', ');
        option.value = index;
        return option;
    }

    #displayHistogram(histoDescr, histogramChartView, chartWithSlider) {
        histogramChartView.displayChart(histoDescr);
        this.#createSlider(
            {
                sliderElement: chartWithSlider.querySelector(".slider"),
                range: {
                    min: 0,
                    max: Object.keys(histoDescr.histogram).length
                },
                orientation: 'vertical',
                height: chartWithSlider.querySelector("canvas").style.height,
                onUpdate: range => histogramChartView.setData(this.#slice(histoDescr, range))
            });
    }

    #slice(histoDescr, { start, endInclusive }) {
        return {
            batchcodes: histoDescr.batchcodes,
            histogram: Utils.sliceDict(histoDescr.histogram, start, endInclusive + 1)
        };
    }

    #createSlider({ sliderElement, range, orientation, height = null, onUpdate }) {
        if ('noUiSlider' in sliderElement) {
            sliderElement.noUiSlider.destroy();
        }
        noUiSlider.create(
            sliderElement,
            {
                start: [range.min, range.max],
                connect: true,
                range: range,
                step: 1,
                orientation: orientation
            });
        sliderElement.noUiSlider.on(
            'update',
            ([start, endInclusive]) =>
                onUpdate(
                    {
                        start: parseInt(start, 10),
                        endInclusive: parseInt(endInclusive, 10)
                    }));
        if (height != null) {
            sliderElement.style.height = height;
        }
    }
}