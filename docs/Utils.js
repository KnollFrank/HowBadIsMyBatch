class Utils {

    // adapted from https://www.w3resource.com/javascript-exercises/fundamental/javascript-fundamental-exercise-88.php
    static median(arr) {
        const mid = Math.floor(arr.length / 2);
        const nums = [...arr].sort((a, b) => a - b);
        return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
    }
}
