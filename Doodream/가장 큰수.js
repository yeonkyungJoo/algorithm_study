function solution(numbers) {
    var answer = numbers.map((number) => number.toString()).sort((a, b) => (b + a) - (a + b)).join("");
    return answer.replace(/^0+/, "0");
}
var numbers = [3, 30, 34, 5, 9];
console.log(solution(numbers));