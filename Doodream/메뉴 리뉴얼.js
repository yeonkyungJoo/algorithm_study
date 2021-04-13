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
function solution(orders, course) {
    var answer = [];
    let obj = {}
    orders = orders.map(e => e.split('').sort().join(''));
    for (let i = 0; i < orders.length; i++) {
        let result = [];
        let arr = orders[i].split('');
        for (let j = 0; j < course.length; j++) {
            result.push(...getCombinations(arr, course[j]));
        }
        obj = result.reduce((acc, e) => {
            let joined = e.join('')
            if (joined in acc) {
                acc[joined] += 1;
            } else {
                acc[joined] = 1;
            } return acc
        }, obj)

    }
    let arr = Object.entries(obj);
    for (let i in course) {
        let arr2 = arr.filter(e => e[0].length === course[i] && e[1] !== 1)
        let max = 0
        if (arr2.length > 0) {
            max = Math.max(...arr2.map(e => e[1]))
        }
        arr2.forEach(e => {
            if (e[1] === max) {
                answer.push(e[0])
            }
        })
    }

    return answer.sort();
}

const getCombinations = function (arr, n) {
    const results = [];
    if (n === 1) return arr.map((e) => [e]);
    arr.forEach((e, idx, origin) => {
        const rest = origin.slice(idx + 1);
        const combinations = getCombinations(rest, n - 1);
        const attached = combinations.map((combination) => [e, ...combination]);
        results.push(...attached);
    });
    return results;
}