/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {
    const n = words.length
    const combined = words.join('')
    const unique = [...new Set(combined)]
    // console.log(combined)

    for (let char of unique){

        if ( (combined.split(char).length - 1)%n != 0 ){
            return false
        }
    }

    return true

};
