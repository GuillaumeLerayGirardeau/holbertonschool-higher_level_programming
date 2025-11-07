#!/usr/bin/node

const firstArg = process.argv[2] ?? 'undefined';
let secondArg = process.argv[3];
if (secondArg === undefined) {
  secondArg = 'undefined';
}
let sentence = firstArg.concat(' is ');
sentence = sentence.concat(secondArg);
console.log(sentence);
