/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Beats 565 of users.
 */
var isAnagram = function(s, t) {
    if (s.length!=t.length){
        return false
    }

    let counter = {}

    for (item of s){

        if (counter[item]){
            counter[item] += 1
        }
        else{
            counter[item] = 1
        }
    }

    for (string of t){
        if (!(string in counter) || counter[string]==0){
            return false
        }
        counter[string] -= 1
    }

    return true
};
