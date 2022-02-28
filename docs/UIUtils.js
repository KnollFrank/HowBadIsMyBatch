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
}
