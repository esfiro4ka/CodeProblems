const countChars = (str, letter) => {
    let new_letter = letter.toLowerCase();
    let new_str = str.toLowerCase();
    let count = 0;
    let i = 0;
    while (i < str.length) {
      if (new_str[i] === new_letter) {
        count += 1;
      }
      i += 1;
    }
    return count;
}

console.log(countChars('HexlEt', 'e')); // 2
