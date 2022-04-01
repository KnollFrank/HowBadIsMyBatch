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

    static getYLabelWithPercent(context) {
        return UIUtils._getLabelWithPercent(context, context.parsed.y);
    }

    static getXLabelWithPercent(context) {
        return UIUtils._getLabelWithPercent(context, context.parsed.x);
    }

    static _getLabelWithPercent(context, value) {
        let label = context.dataset.label || '';

        if (label) {
            label += ': ';
        }
        if (value !== null) {
            label += value.toFixed(1) + "%";
        }
        return label;
    }

    static getPercentageScale(label) {
        return {
            min: 0,
            max: 100,
            title: {
                display: true,
                text: label
            },
            ticks: {
                callback: value => value + "%"
            }
        }
    }
}
