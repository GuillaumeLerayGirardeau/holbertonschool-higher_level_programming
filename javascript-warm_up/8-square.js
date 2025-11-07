#!/usr/bin/node

/* Prints a square */

const squareSize = parseInt(process.argv[2]);
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let ySize = 0; ySize < squareSize; ySize++) {
    for (let xSize = 0; xSize < squareSize; xSize++) {
      process.stdout.write('#');
    }
    console.log('');
  }
}
