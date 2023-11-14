#!/usr/bin/node
const args = process.argv;
const message = (args.length === 3) ? 'Argument found' : (args.length > 3) ? 'Arguments found' : 'No argument';

console.log(message);
