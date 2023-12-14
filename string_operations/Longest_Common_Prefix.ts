//86% percentile performance
function longestCommonPrefix(strs: string[]): string {
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
