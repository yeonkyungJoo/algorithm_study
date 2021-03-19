function solution(s) {
    var answer = true;
    let sArr = s.split('');

    // 주어진 s가 짝수가 아니거나 처음이 '(' 마지막이 ')' 로 끝나지 않는 경우 x
    if (s.length % 2 !== 0 || sArr[0] !== '(' || sArr[s.length - 1] !== ')') {
        answer = false;
        return answer;
    }

    // '(' ')' 의 갯수가 동일하지 않은경우 x
    let openLetterCount = 0;
    let closeLetterCount = 0;

    sArr.map(x => {
        x === '(' ? openLetterCount++ : closeLetterCount++;
    })

    if (openLetterCount !== closeLetterCount) {
        answer = false;
        return answer;
    }

    // 문자열에서 괄호가 닫힌 경우를 모두 제거하고 (반복)제거 후 문자열로 통합
    sStr = s.split('()').join('');
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

let s = "()))((()";
console.log(solution(s));