function solution(n) {
    var answer = 0;
    var sum = 0;
    var j = 0;
    for (var i = 1; i < n + 1; i++) {
        sum = 0;
        j = i;
        while (sum <= n) {
            sum += j;
            if (sum === n) answer++;
            j++;
        }
    }
    return answer;
}

console.log(solution(15))
