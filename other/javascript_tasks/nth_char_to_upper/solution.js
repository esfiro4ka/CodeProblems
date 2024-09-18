const makeItFunny = (str, n) => {
    let result = '';
    let i = 0;
    while (i < str.length) {
      if ((i+1) % n === 0){
        let new_str = str[i].toUpperCase()
        result += new_str;
      } else {
      result += str[i];
      }
      i += 1;
    }
    return result;
}

document.write(makeItFunny('I never look back', 3)) // I NevEr LooK bAck
