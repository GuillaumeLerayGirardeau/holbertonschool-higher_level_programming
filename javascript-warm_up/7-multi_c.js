#!/usr/bin/node

/* Prints x times "C is fun" */

let printNumber = parseInt(process.argv[2]);
if (isNaN(printNumber)) {
  console.log('Missing number of occurrences');
} else {
  while (printNumber >= 0) {
    console.log('C is fun');
    printNumber--;
  }
}
