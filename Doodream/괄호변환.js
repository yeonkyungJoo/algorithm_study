function solution(p) {
    var answer = "";
    if (p.length === 0) return p;
    p = p.split('');
    var u = "";
    var v = "";

    var openCount = 0;
    var closeCount = 0;

    while (true) {
        var tmp = p.shift();

        if (tmp === "(") {
            openCount++;
            u += tmp;
        } else {
            closeCount++;
            u += tmp;
        }
        if (openCount === closeCount) break;
        //console.log(1);
    }
    v = p.join('');

    if (isCorrectString(u)) answer = solution(v);
    else {
        answer += "(";
        answer += solution(v);
        answer += ")";
        u = u.split('');
        u.shift();
        u.pop();
        var tmp = "";
        for (var i = 0; i < u.length; i++) {
            u[i] === "(" ? tmp += ")" : tmp += "(";
        }
        answer += tmp;
        //console.log(2);

        return answer;
    }
    //console.log(3);
    return u + answer;
}

// s는 균형 잡힌 문자열
function isCorrectString(s) {
    var answer = true;
    // 문자열에서 괄호가 닫힌 경우를 모두 제거하고 (반복)제거 후 문자열로 통합
    var sStr = s.split('()').join('');
    // 해당 문자열이 () 혹은 없는 경우 true
    if (sStr === '()' || sStr === '') {
        return answer;
    }

    // false 인 경우는 '()))((()' 이런 경우 이므로 바로 위코드를 수행하면 ')))(((' 이렇게 되어 거른다. 
    if (sStr[0] !== '(' || sStr[sStr.length - 1] !== ')') {
        answer = false;
        return answer;
    }
    return answer;
}

console.log(solution("()))((()"));
