const invertCase = (str) => {
    result = ''
    for (i=0; i<str.length; i++) {
        if (str[i] === str[i].toUpperCase()) {
            result += str[i].toLowerCase()}
            else {result += str[i].toUpperCase()}
    }
    return result;
}

document.write(invertCase('Hello, World!'))  // hELLO, wORLD!
document.write(invertCase('I loVe JS'))  // i LOvE js
