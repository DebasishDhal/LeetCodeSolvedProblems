/**
 * @param {number} num
 * @return {number}
 Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.

Constraints:

10 <= num <= 109
 */
var splitNum = function(num) {
    let numList = num.toString().split('').sort((a, b) => a - b)

    // console.log(numList)

    let num1 = ''
    let num2 = ''

    let pos = 0

    while (pos<numList.length){ //I accidentally wrote legnth instead of length, and JS is not even throwing errors. Weird.
        num1 += numList[pos]
        pos += 1

        if (pos<numList.length){
            num2 += numList[pos]
            pos += 1
        }
    }
    console.log(num1)
    console.log(num2)
    return parseInt(num1)+parseInt(num2)
};
