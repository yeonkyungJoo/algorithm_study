function solution(s) {
    var reCount = 0;
    var zeroCount = 0;
    while (s.length > 1) {
        var beforeLength = s.length;
        s = s.split('0').join('');
        var afterLength = s.length;
        zeroCount += beforeLength - afterLength;
        s = afterLength.toString(2);
        reCount++;
    }
    var answer = [reCount, zeroCount];
    return answer;
}

var s = "110010101001";
console.log(solution(s));

