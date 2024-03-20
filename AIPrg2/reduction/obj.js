const students = {
    "student1": {id: 1, "name": "John", "age": 20},
    "student2": {id: 2, "name": "Jane", "age": 21},
    "student3": {id: 3, "name": "Bob", "age": 22},
};
// result: {
//     '1': { id: 1, name: 'John', age: 20 },
//     '2': { id: 2, name: 'Jane', age: 21 },
//     '3': { id: 3, name: 'Bob', age: 22 }
//   }
function reducer(accumulator, current_value) {
    console.log("accumulator:", accumulator);
    console.log("current_value:", current_value);
    accumulator[students[current_value].id] = students[current_value];
    return accumulator;
}

initial_value = {};

const result = Object.keys(students).reduce(reducer, initial_value);
console.log("result:", result);