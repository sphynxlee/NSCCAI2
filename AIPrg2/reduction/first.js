// console.log('hello world');

// const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// nums.reduce((acc, num) => {
//     console.log(acc, num);
//     return acc + num;
// }, 0);


initial_value = 0;
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

print = console.log;
print(nums.reduce(reducer, initial_value));

function reducer(accumulator, current_value) {
    print("accumulator:", accumulator);
    print("current_value:", current_value);
    return accumulator + current_value;
}