function solution(msg) {
    var msgStr = JSON.parse(JSON.stringify(msg));
    function longestWord(count) {
        var maxLength = dict[dict.length - 1].length
        while (maxLength > 0) {
            var word = msgStr.substring(count, count + maxLength);
            if (dict.includes(word)) {
                return word;
            }
            maxLength--;
        }
    }

    msg = msg.split('');

    var answer = [];
    const dict = [];
    for (let i = 0; i < 26; i++) {
        dict[i] = String.fromCharCode([i + 65]);
    }
    var count = 0;
    var currentEnter = longestWord(count);
    var nextEnter = msg[count + 1];

    while (true) {
        if (count > msg.length) break;
        // 현재 입력이 사전에 있나?
        if (dict.includes(currentEnter)) {
            // 다음번 입력이 포함된 길이가 사전에 있나?
            if (!dict.includes(currentEnter + nextEnter)) {
                // 출력
                answer.push(dict.indexOf(currentEnter) + 1);
                // 사전추가
                dict.push(currentEnter + nextEnter);
                count += currentEnter.length;

                currentEnter = longestWord(count);
                if (currentEnter === undefined) {
                    return answer;
                }
                if (count + currentEnter.length > msg.length) {
                    answer.push(dict.indexOf(currentEnter) + 1);
                    return answer;
                }
                nextEnter = msg[count + currentEnter.length];
                continue;
            }
        }
    }
}



var msg = 'KAKAO';
console.log(solution(msg));