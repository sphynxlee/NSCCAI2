it(
    'should add two numbers',
    () => {
        const add = require('./add');
        expect(add(1, 2)).toEqual(3);
    }
);