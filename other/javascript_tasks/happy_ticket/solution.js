// const sumOfSquareDigits = (number) => {
//     return String(number)             // Преобразуем число в строку
//         .split('')                    // Разбиваем строку на массив символов
//         .reduce((sum, digit) => sum + (parseInt(digit, 10) ** 2), 0); // Преобразуем каждую цифру в число, возводим в квадрат и суммируем
// }

// то же самое, что:
//     const str_num = String(number);
//     const digits_array = str_num.split(''); // Разбиваем число на отдельные цифры
//     let sum = 0;
//     for (let i=0; i<digits_array.length; i++) {
//         digit = digits_array[i];
//         sum = sum + parseInt(digit, 10) ** 2
//     }

//     return sum
// }

// console.log(sumOfSquareDigits(123)); // 14 (1^2 + 2^2 + 3^2)
// console.log(sumOfSquareDigits(456)); // 77 (4^2 + 5^2 + 6^2)
// console.log(sumOfSquareDigits(789)); // 194 (7^2 + 8^2 + 9^2)


const sumOfSquareDigits = (number) => {
    const str_num = String(number);
    const digits_array = str_num.split('');

    let sum = 0;
    for (let i=0; i<digits_array.length; i++) {
        digit = digits_array[i];
        sum += parseInt(digit, 10) ** 2
    }

    return sum
}

const isHappy = (number) => {
    let count = 0;
    while (count <= 10) {
        number = sumOfSquareDigits(number);
        if (number === 1) {
            return true
        }
        count += 1
    }
    return false;
}
console.log(isHappy(7));
