const reverseInt = (number) => {
    let abs_number = Math.abs(number);
    let str_number = abs_number.toString();
    let result = '';

    if (abs_number !== number) {
        result += '-';
    }
    for (let i=str_number.length - 1; i >= 0; i--) {
        result += str_number[i];
    }
    return parseInt(result);
}


console.log(reverseInt(13)) // 31
console.log(reverseInt(-123)) // -321
console.log(reverseInt(8900)) // 98
