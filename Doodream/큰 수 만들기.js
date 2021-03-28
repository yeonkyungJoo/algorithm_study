function solution(number, k) {
    var stack = [];
    var answer = '';

    for (let i = 0; i < number.length; i++) {
        var max = number[i];
        while (k > 0 && stack[stack.length - 1] < max) {
            stack.pop();
            k--;
        }
        stack.push(max);
    }

    stack.splice(stack.length - k, k);
    answer = stack.join('');
    return answer;
}

var number = "4177252841";
var k = 4;
console.log(solution(number, k));
