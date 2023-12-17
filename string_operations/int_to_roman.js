/**
 * @param {number} num
 * @return {string}
 Not an efficient algorithm but it works
 */
var intToRoman = function(num) {
    let dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C', 90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

    let roman = '';
    for (let number of Object.keys(dic).reverse()) {
        number = parseInt(number);
        let quotient = Math.floor(num / number);
        roman += dic[number].repeat(quotient);
        num -= quotient * number;
    }

    return roman;
};
