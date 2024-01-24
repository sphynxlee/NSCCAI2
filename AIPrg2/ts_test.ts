class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    sayHello(): void {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
    }

    sayGoodbye(): void {
        console.log(`Goodbye from ${this.name}.`);
    }
}

let p1 = new Person("Bob", 22);
p1.sayHello();
p1.sayGoodbye();