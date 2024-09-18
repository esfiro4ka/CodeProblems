const isPerfect = (number) => {
    let sum = 0;
    for (let i = 1; i < number; i++) {
        if (number % i === 0) {
            sum += i;
        }
    }
    return sum === number;
}

console.log(isPerfect(6));  // true
console.log(isPerfect(7));  // false
