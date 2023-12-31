/**
 * @param {string} s
 * @return {number}
 
 */
var maxLengthBetweenEqualCharacters = function(s) {
    let occurence = {};

    for (let i = 0; i < s.length; i++) {
        if (!(s[i] in occurence)) {
            occurence[s[i]] = [i];
        } else {
            occurence[s[i]].push(i);
        }
    }

    let maxLen = 0;
    let repeat = false;

    for (let item of Object.values(occurence)) {
        if (item.length < 2) {
            continue;
        } else {
            repeat = true;
        }

        let largestStretch = item[item.length - 1] - item[0] - 1;
        maxLen = Math.max(maxLen, largestStretch);
    }

    if (repeat) {
        return maxLen;
    } else {
        return -1;
    }
};
