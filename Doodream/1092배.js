const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

function solution() {
  const inputs = input.split("\n");
  const n = Number(inputs[0]);
  const cranes = inputs[1]
    .split(" ")
    .map((a) => +a)
    .sort((a, b) => b - a);

  const box = Number(inputs[2]);

  const boxes = inputs[3]
    .split(" ")
    .map((a) => +a)
    .sort((a, b) => b - a);

  const checked = new Array(box).fill(undefined).map((a) => false);
  const positions = new Array(n).fill(undefined).map((a) => 0);

  let time = 0;
  let count = 0;

  if (boxes[0] > cranes[0]) {
    time = -1;
    count = box;
  }

  while (true) {
    if (count === box) {
      break; // 박스 다옮김
    }
    for (let i = 0; i < cranes.length; i++) {
      while (positions[i] < box) {
        if (!checked[positions[i]] && cranes[i] >= boxes[positions[i]]) {
          checked[positions[i]] = true;
          positions[i] += 1;
          count += 1;
          break;
        }
        positions[i] += 1;
      }
    }
    time += 1;
  }
  console.log(time);
}

solution();
