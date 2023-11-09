class Sets {

    static filterSet(set, predicate) {
        return new Set([...set].filter(predicate));
    }

    static union(sets) {
        return sets.reduce(
            (union, set) => new Set([...union, ...set]),
            new Set());
    }

    static intersection(set1, set2) {
        return new Set([...set1].filter(x => set2.has(x)));
    }

    static isEmpty(set) {
        return set.size == 0;
    }
}