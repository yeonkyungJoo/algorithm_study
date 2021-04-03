function solution(s) {
    s = s.toLowerCase();
    s = s.split(" ");


    for (let i = 0; i < s.length; i++) {
        var firstAsciNum = s[i].charCodeAt(0);
        if (firstAsciNum >= 97 && firstAsciNum <= 122) {
            s[i] = s[i].split('');
            s[i][0] = String.fromCharCode(firstAsciNum - 32);
            s[i] = s[i].join('');
        }
    }

    var answer = s.join(' ');
    return answer;
}

var s = "3people unFollowed me";
console.log(solution(s));