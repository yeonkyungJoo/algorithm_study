const key = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}
let idx = 27;
function solution(msg) {
    let answer = [];
    for (let i = 0; i < msg.length; i) {
        let w = msg[i];
        let c = msg[i + 1];
        let newW = add(msg, i, w, c, 0);
        // 반환된 문자 w의 색인 번호를 추가하고
        // w의 길이만큼 건너뛰도록 i에 크기를 더한다
        answer.push(key[newW]);
        i += newW.length;
    }
    return answer;
}
function add(msg, i, w, c, cnt) {
    // w+c가 사전에 있으면 그다음 단어를 붙어 다시 확인하고
    // w+c가 사전에 없으면 사전에 추가하고 문자 w를 반환한다
    if (key[w + c] === undefined) {
        key[w + c] = idx++;
        console.log(w, c, key[w], key[w + c])
        return w;
    } else {
        cnt++;
        let newW = w + c;
        let newC = msg[i + 1 + cnt];
        return add(msg, i, newW, newC, cnt);
    }
}


var msg = 'KAKAO';
console.log(solution(msg));