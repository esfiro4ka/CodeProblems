const fizzBuzz = (begin, end) => {
    let result = '';
    for (let i = begin; i <= end; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            result += 'FizzBuzz\n';
        } else if (i % 3 === 0) {
            result += 'Fizz\n';
        } else if (i % 5 === 0) {
            result += 'Buzz\n';
        } else {
            result += i + '\n';
        }
    }
    return result.trim(); // возврат строки без лишнего символа новой строки в конце
}

console.log(fizzBuzz(11, 20));
