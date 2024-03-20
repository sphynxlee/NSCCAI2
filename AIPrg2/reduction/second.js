const data = [
    {id: 1, name: "Dean"},
    {id: 2, name: "Fleur"},
    {id: 3, name: "Lia"},
    {id: 4, name: "Sophie"},
];
// {
//     1: {id: 1, name: "Dean"},
//     2: {id: 2, name: "Fleur"},
//     ...
// }
function reducer(accumulator, current_value) {
    console.log("accumulator:", accumulator);
    console.log("current_value:", current_value);
    accumulator[current_value.id] = current_value;
    return accumulator;
}
const result = data.reduce(reducer, {});
console.log("result:", result);