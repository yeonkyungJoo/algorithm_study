function solution(citations) {

    //https://programmers.co.kr/learn/courses/30/lessons/42747?language=javascript

    let arrH = [];

    // h를 0부터 차례 차례 증가시킨다.
    for (let h = 0; h <= citations.length; h++) {
        let count = 0;
        for (let i = 0; i < citations.length; i++) {
            // h번이상 인용되었다면 count++
            if (citations[i] >= h) {
                count++
            }
        }
        // h번이상 인용된 논문의 수가 h이상이면 해당 h를 arrH에 추가
        if (count >= h) {
            arrH.push(h);
        } else {
            break;
        }
    }

    // 작은순으로 추가되므로 가장 마지막에 있는 원소가 가장 큰 H
    var answer = arrH[arrH.length - 1];
    return answer;
}

let citations = [0, 0, 0];
console.log(solution(citations));