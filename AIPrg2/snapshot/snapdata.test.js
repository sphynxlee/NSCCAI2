const myData = require('./snapdata');

test('That the data didn\'t change', () => {
    expect(myData).toMatchSnapshot();
});

// npm init -y
// npm install jest
// npm test

// npm list or npm uninstall jest
// npm install -g vitest
// npm list -g

// npm test

// npx jest --updateSnapshot