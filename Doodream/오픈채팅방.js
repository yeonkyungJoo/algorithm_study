function solution(record) {
    var answer = [];
    var newArr = record.map(str => str.split(" "));

    var nickNameSet = {};
    for (var i = 0; i < newArr.length; i++) {
        if (newArr[i].length === 3) {
            nickNameSet[newArr[i][1]] = newArr[i][2];
        }
    }

    for (var i = 0; i < newArr.length; i++) {
        if (newArr[i][0] === 'Enter') {
            answer.push(nickNameSet[newArr[i][1]] + '님이 들어왔습니다.');
        } else if (newArr[i][0] === 'Leave') {
            answer.push(nickNameSet[newArr[i][1]] + '님이 나갔습니다.');
        }
    }

    return answer;
}

var record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"];
console.log(solution(record));