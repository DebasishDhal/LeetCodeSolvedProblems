// My solution, not very efficient
var decodeMessage = function(key, message) {
    let mapDict = {' ': ' '}
    let doneList = [' ']
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    var pos = 0

    for (let char of key){
        if (doneList.includes(char)){ //This line can be optimized by utilizing mapDict.hasOwnProperty instead
            continue;
        }

        mapDict[char] = alphabet[pos]
        pos += 1
        doneList.push(char)
    }
    // console.log(doneList)
    // console.log(mapDict)

    let decoded = ''
    for (let char of message){
        // console.log (char,mapDict[char])
        decoded += mapDict[char]
    }
    return decoded
};

// Elegant solution
var decodeMessage = function(key, message) {
    let map = {" ": " "};
    let charCode = 'a'.charCodeAt(0);
    for(let char of key) {
        if(map[char]) continue;
        map[char] = String.fromCharCode(charCode++);
    }
    return message.split('').map(char => map[char]).join('');
};
