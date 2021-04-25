const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

function solution() {
  let answer = 0;
  const inputs = input[0].split(" ").map(Number);
  let [a, b, c, x, y] = inputs;
  if (c < (a + b) / 2) {
    const cCount = x < y ? x * 2 : y * 2;
    answer = Math.min(
      a * (x - cCount / 2) + b * (y - cCount / 2) + c * cCount,
      c * Math.max(x, y) * 2
    );
  } else {
    answer = a * x + b * y;
  }
  return answer;
}

console.log(solution());
