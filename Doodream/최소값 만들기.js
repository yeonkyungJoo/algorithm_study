function solution(A, B) {
    var answer = 0;
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);

    for (var i = 0; i < A.length; i++) {
        answer += A[i] * B[i];
    }
    return answer;
}

var A = [1, 4, 2];
var B = [5, 4, 4];

console.log(solution(A, B))