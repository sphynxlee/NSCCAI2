let Dean = {name: "Dean", age: 52};
let newCreature = Dean;
console.log(Dean, newCreature);
// deep copy
newCreature = JSON.parse(JSON.stringify(Dean));
newCreature.age = 53;

console.log(Dean, newCreature);