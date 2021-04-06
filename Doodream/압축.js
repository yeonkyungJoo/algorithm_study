function solution(msg) {
    msg = msg.split('');

    var answer = [];
    const dict = [];
    for (let i = 0; i < 26; i++) {
        dict[i] = String.fromCharCode([i + 65]);
    }

    for (var count = 0; count < msg.length; count++) {
        var currentEnter = msg[count];
        var nextEnter = msg[count + 1];

        while (dict.includes(currentEnter + nextEnter) && count < msg.length) {
            count++;
            currentEnter = currentEnter + nextEnter;
            nextEnter = msg[count + 1];
        }

        answer.push(dict.indexOf(currentEnter) + 1);
        dict.push(currentEnter + nextEnter);
    }

    return answer;
}



var msg = 'KAKAO';
console.log(solution(msg));