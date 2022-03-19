class UIUtils {

    static instantiateTemplate(templateId) {
        return document.getElementById(templateId).content.firstElementChild.cloneNode(true);
    }

    static createChartViewElementWithHeading(heading) {
        const chartViewElement = UIUtils.instantiateTemplate('template-ChartView');
        chartViewElement.querySelector(".heading").textContent = heading;
        return {
            chartViewElement: chartViewElement,
            canvas: chartViewElement.querySelector(".canvas")
        };
    }

    static getSelectedOption(selectElement) {
        return selectElement.options[selectElement.selectedIndex];
    }

    static labelWithPercentCallback(context) {
        let label = context.dataset.label || '';

        if (label) {
            label += ': ';
        }
        if (context.parsed.y !== null) {
            label += context.parsed.y.toFixed(1) + "%";
        }
        return label;
    }
}
