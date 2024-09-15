const sumOfSquareDigits = (number) => {
    let result = 0;
    let count = 0;
    while (count !== 10) {
        for (let i=0; i<number.length; i++) {
            result += number[i] * number[i];
        }
        if (result === 1) {
            return true;
        }
        number = result.toString();
        count +=1;
        result = 0;
    }
    return false;
}

console.log(sumOfSquareDigits('6')); // false
console.log(sumOfSquareDigits('7')); // true

// 7   => 7^2 = 49,
// 49  => 4^2 + 9^2 = 16 + 81 = 97,
// 97  => 9^2 + 7^2 = 81 + 49 = 130,
// 130 => 1^2 + 3^2 + 0^2 = 10,
// 10  => 1^2 + 0^2 = 1.
