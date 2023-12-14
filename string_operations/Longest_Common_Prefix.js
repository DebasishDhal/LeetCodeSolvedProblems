/**
 * @param {string[]} strs
 * @return {string}
 96% percentile

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1: Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
 */
var longestCommonPrefix = function(strs) {
    let words = strs.sort()
    let first = words[0]
    let last = words[strs.length-1]

    let res = ''
    for (let i = 0; i < Math.min(first.length, last.length); i++){

        if (first[i] != last[i]) {
            return res
        }
        
        else {
            res += first[i]
        }
    }

    return res
};
