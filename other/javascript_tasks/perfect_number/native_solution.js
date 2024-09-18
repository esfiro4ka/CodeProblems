const isPerfect = (number) => {
    let result_list = [];
    for (let i=1; i < number; i++) {
        if (number % i === 0) {
            result_list.push(i)
        }
    }
    let sum = 0;
    for (let j=0; j < result_list.length; j++) {
        sum += result_list[j]
    }
    if (sum === number) {
        return true
    } else {
        return false
    }
}

console.log(isPerfect(6));  // true
console.log(isPerfect(7));  // false
