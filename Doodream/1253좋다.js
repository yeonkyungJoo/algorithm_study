"use strict";

// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString();

function solution(input) {
  const answer = [];
  const inputs = input.split("\n");
  const N = Number(inputs[0]);
  const arrA = inputs[1].split(" ").map((a) => Number(a));
  arrA.sort((a, b) => a - b);
  console.log(arrA);

  let index = 0;
  while (index < arrA.length) {
    let left = 0;
    let right = arrA.length - 1;
    while (left < right) {
      if (index === left) {
        left += 1;
        continue;
      }
      if (index === right) {
        right -= 1;
        continue;
      }
      const sum = arrA[left] + arrA[right];
      const find = arrA[index];
      if (sum < find) left += 1;
      else if (sum > find) right -= 1;
      else {
        answer.push(find);
        break;
      }
    }
    index += 1;
  }
  return answer.length;
}

console.log(
  solution(`3
0 0 0`)
);
