// Create a program named 1-stdin.js that
// will be executed through command line:

const readline = require('node:readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

console.log("Welcome to Holberton School, what is your name?")

rl.question(`What's your name?\n`, name => {
    console.log(`Your name is: ${name}`);
    rl.close();
});

process.on('exit', () => {
    console.log("This important software is now closing");
});
