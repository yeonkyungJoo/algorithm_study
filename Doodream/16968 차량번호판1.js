const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

function solution() {
  let answer = 1;

  const inputs = input[0].split("");
  for (let i = 0; i < inputs.length; i++) {
    const current = inputs[i];
    if (i === 0) {
      current === "c" ? (answer *= 26) : (answer *= 10);
      continue;
    }

    if (inputs[i - 1] === current) {
      current === "c" ? (answer *= 25) : (answer *= 9);
      continue;
    } else {
      current === "c" ? (answer *= 26) : (answer *= 10);
      continue;
    }
  }
  return answer;
}

console.log(solution());
