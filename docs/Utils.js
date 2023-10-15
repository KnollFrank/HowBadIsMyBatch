class Utils {

    // adapted from https://www.w3resource.com/javascript-exercises/fundamental/javascript-fundamental-exercise-88.php
    static median(arr) {
        const mid = Math.floor(arr.length / 2);
        const nums = [...arr].sort((a, b) => a - b);
        return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
    }

    static sum(numbers) {
        return numbers.reduce((a, b) => a + b, 0);
    }

    static getKeysAlignedWithValues(dict) {
        const keys = [];
        const values = [];
        for (const [key, value] of Object.entries(dict)) {
            keys.push(key);
            values.push(value);
        }
        return { 'keys': keys, 'values': values };
    }

    static sliceDict(dict, start, end) {
        return Object.fromEntries(Object.entries(dict).slice(start, end));
    }

    static convertDict2CSV(dict) {
        return Dict2CsvConverter.convertDict2CSV(dict);
    }
}
