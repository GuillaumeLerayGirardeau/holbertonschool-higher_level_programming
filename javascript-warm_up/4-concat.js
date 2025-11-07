#!/usr/bin/node

let firstArg = process.argv[2];
if (firstArg === undefined) {
  firstArg = 'undefined';
}
let secondArg = process.argv[3];
if (secondArg === undefined) {
  secondArg = 'undefined';
}
let sentence = firstArg.concat(' is ');
sentence = sentence.concat(secondArg);
console.log(sentence);
