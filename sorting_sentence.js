/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let result = []
    let word = ""
    for(let char of s){
        if(typeof (+char) == 'number') result[(char - 1)] = word
        if(char === ' ') word = ""
        else word += char
    }
    return result.join(' ')
};