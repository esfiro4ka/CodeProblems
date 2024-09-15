const encrypt = (str) => {
    let result = '';
    for (i=0; i+2 <= str.length; i+=2) {
      result = `${result}${str[i+1]}${str[i]}`;
    }
    if (str.length % 2 !== 0) {
      result +=`${str[str.length-1]}`
    }
    return result;
}

document.write(encrypt('attack')); // 'taatkc'
