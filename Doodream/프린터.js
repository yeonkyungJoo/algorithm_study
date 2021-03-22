function solution(priorities, location) {
    let printOrder = [];
    // 프린트된 문서를 순서대로 모아 놓는배열
    let printOrderLocation = [];
    // 프린트된 문서의 원래 순서를 기록해놓는 배열
    let prioritiesLocation = [];
    // 프린트 된 문서의 중요도의 위치를 기록해 놓는 배열

    for (let i = 0; i < priorities.length; i++) {
        prioritiesLocation[i] = i;
    }
    // J의 위치를 추적하기 위해서 원래 J의 인덱스를 J와 완전히 동일하게 움직인다. 
    // 위치는 [0, 1, 2, 3, ..., priorities.length - 1]로 기록되며 J가 이동하는 순서랑 완벽히 동일하게 움직인다. 

    while (priorities.length !== 0) {
        // 가장 앞의 문자가 J가 된다.
        let J = priorities.shift();

        // J의 원래 위치를 추적하기 위해서 J와 동일하게 움직인다. 
        let Jlocation = prioritiesLocation.shift();
        if (J < Math.max(...priorities)) {
            // 대기열의 문서중에 J보다 중요한 것이 있다면 
            priorities.push(J);
            prioritiesLocation.push(Jlocation);
        } else {
            // 없다면 
            printOrder.push(J);
            printOrderLocation.push(Jlocation);
        }
    }

    // 원래 J의 위치를 추적해서 + 1을 해주면 답. 
    var answer = printOrderLocation.indexOf(location) + 1;
    return answer;
}

let priorities = [1, 1, 9, 1, 1, 1];
// 전역 객체에 변수중에 location이 들어가있어서 재 선언시 호이스팅 문제가 발생, location 변수명을 다르게 해준다. 
let location2 = 0;

console.log(solution(priorities, location2));

