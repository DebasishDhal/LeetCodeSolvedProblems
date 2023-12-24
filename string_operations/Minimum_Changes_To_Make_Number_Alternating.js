/**
 * @param {string} s
 * @return {number}
 You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
 */
var minOperations = function(s) {
    let changes0101 = 0
    let changes1010 = 0
    let pos = 0
    for (let char of s){
        if (parseInt(char) != pos%2){
            changes0101 += 1
        }

        else{
            changes1010 += 1
        }

        pos += 1
    }

    return Math.min(changes1010,changes0101)
};
