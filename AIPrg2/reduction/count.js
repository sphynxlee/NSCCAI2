const names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'];

function reducer(accumulator, current_value) {
    if (accumulator[current_value]) {
        accumulator[current_value]++;
    } else {
        accumulator[current_value] = 1;
    }
    return accumulator;
}

initial_value = {};

result = names.reduce(reducer, initial_value);
console.log(result);