#!/usr/bin/node

if ((process.argv).length < 4) {
  console.log(0);
} else {
  const arg = process.argv.slice(2).map(x => Number(x));
  const orderList = arg.sort((a, b) => b - a);
  console.log(orderList[1]);
}
