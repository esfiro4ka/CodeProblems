const convertText = (str) => {
    if (str === '') {
      return '';} else if (str[0] === str[0].toUpperCase()) {
        return str;} else {
          return reverse(str)}
};

convertText('Hello'); // 'Hello'
convertText('hello'); // 'olleh'
convertText(''); // ''
