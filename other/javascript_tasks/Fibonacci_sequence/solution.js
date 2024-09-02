const fib = (number) => {
    let result = 0;
    let first = 0;
    let second = 1;
    for (let i=2; i <= number; i++) {
        result = first + second;
        first = second;
        second = result;
    }
    return result;
}

console.log(fib(3))  // 2
console.log(fib(5))  // 5
console.log(fib(10)) // 55
