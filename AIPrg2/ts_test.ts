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

    // work is a generic function that can take any object that has a name and age property
    work<Type extends { toString(): string }>(obj: Type): void {
        console.log(`${obj.toString()} is working.`);
    }
}

let p1 = new Person("Bob", 22);
p1.sayHello();
p1.sayGoodbye();
p1.work(p1);