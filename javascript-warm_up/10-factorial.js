#!/usr/bin/node

function factorial (num) {
  let result = 0;
  if (num > 1) {
    result = factorial(num - 1);
  }
  if (num === 1) {
    return (1);
  }
  return (num * result);
}

const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log(0);
} else {
  console.log(factorial(number));
}
