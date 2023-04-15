class ElementWithSingleChangeEventListener {

    element;
    #changeEventListenerOfElement;

    constructor(element) {
        this.element = element;
    }

    setSingleChangeEventListener(singleChangeEventListener) {
        const eventType = 'change';
        if (this.#changeEventListenerOfElement !== undefined) {
            this.element.removeEventListener(eventType, this.#changeEventListenerOfElement);
        }
        this.element.addEventListener(eventType, singleChangeEventListener);
        this.#changeEventListenerOfElement = singleChangeEventListener;
    }
}
