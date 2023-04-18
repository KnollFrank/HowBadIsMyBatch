class NumberWithBarElementFactory {

    static createNumberWithBarElement({ number, barLenInPercent }) {
        const numberWithBarElement = UIUtils.instantiateTemplate('template-number-with-bar');

        const barElement = numberWithBarElement.querySelector('.bar');
        barElement.style.width = barLenInPercent.toString() + "%";

        const numberElement = numberWithBarElement.querySelector('.number');
        numberElement.textContent = number;

        return numberWithBarElement;
    }
}