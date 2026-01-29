#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  let max = numbers[0];
  let second = -Infinity;

  for (const num of numbers) {
    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num < max) {
      second = num;
    }
  }

  console.log(second);
}
