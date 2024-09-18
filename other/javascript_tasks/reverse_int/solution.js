const reverseInt = (number) => {
    let isNegative = number < 0;
    let absNumber = Math.abs(number);

    let reversedStr = absNumber.toString().split('').reverse().join('');

    let reversedNumber = parseInt(reversedStr);
    return isNegative ? -reversedNumber : reversedNumber;
}

console.log(reverseInt(13));   // 31
console.log(reverseInt(-123)); // -321
console.log(reverseInt(8900)); // 98
