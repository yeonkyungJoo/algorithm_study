function solution(numbers, target) {
    let answer = 0;

    // 문제상 numbers 각각의 원소들이 + - 인 경우로 총 2의 numbers.length 제곱 만큼의 경우의 수발생
    // 하나의 원소당 2가지의 경우의 수가 발생하므로 나뭇가지식으로 재귀를 돌린다.

    const getSum = (index, sum) => {
        // index는 numbers의 원소 인덱스
        // sum은 첫번째 원소 +- 두번쨰 원소 .. 등등 계속 더하거나 빼며 결과를 이어나간다.
        if (index < numbers.length) {
            getSum(index + 1, sum + numbers[index]);
            getSum(index + 1, sum - numbers[index]);
            // 모두 원소를 더하거나 뻇을떄 결과값이 target과 같다면 답 추가
        } else {
            if (sum === target) {
                answer++;
            }
        }
    }
    //재귀의 인덱스는 처음부터 시작하며 시작값은 0이다.
    getSum(0, 0);
    return answer;
}

let numbers = [1, 1, 1, 1, 1];
let target = 3;
console.log(solution(numbers, target));
