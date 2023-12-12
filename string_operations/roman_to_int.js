/**
Quite slow, beats only 6% of users in runtime. This algo worked well in Python although.
 **/

var romanToInt = function(s) {
    const romanDict = {
        'CM': 900, 'XC': 90, 'IV': 4, 'IX': 9, 'XL': 40, 'CD': 400,
        // 'I': 1, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'V': 5
    };

    let res = 0;

    for (const [key, value] of Object.entries(romanDict)) {
        while (s.includes(key)) {
            res += value;
            s = s.replace(key, 'q');
        }
    }
    console.log(s)
    res += (s.split('M').length - 1) * 1000;
    res += (s.split('D').length - 1) * 500;
    res += (s.split('L').length - 1) * 50;
    res += s.split('I').length - 1;
    res += (s.split('X').length - 1) * 10;
    res += (s.split('C').length - 1) * 100;
    res += (s.split('V').length - 1) * 5;


    return res;

};
