function solution(progresses, speeds) {
    var answer = [];
    let remainDays = [];
    // 남은 일수를 계산
    for (let i = 0; i < progresses.length; i++) {
        let day = 1;

        while (true) {
            progresses[i] += speeds[i];
            if (progresses[i] < 100) day++;
            else {
                remainDays.push(day);
                break;
            }
        }
    }
    console.log(remainDays);
    // 남은 일수들을 
    let publish = remainDays[0];
    let count = 1;
    for (let i = 1; i < remainDays.length; i++) {
        if (publish < remainDays[i]) {
            answer.push(count);
            count = 0;
            publish = remainDays[i];
        }
        count++;
    }
    if (count > 0) answer.push(count);
    return answer;
}

var progresses = [95, 90, 99, 99, 80, 99];
var speeds = [1, 1, 1, 1, 1, 1];
console.log(solution(progresses, speeds))