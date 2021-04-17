function solution(n, words) {
    let answer = [];
    let number = 0;
    let order = 0;

    for (let i = 1; i < words.length; i++) {
        let subArr = words.slice(0, i);
        if ((words[i - 1].substring(words[i - 1].length - 1) !== words[i][0]) || (subArr.some(word => word === words[i]))) {
            if ((i + 1) % n === 0) {
                number = n;
            } else {
                number = (i + 1) % n;
            }
            order = Math.ceil((i + 1) / n);
            break;
        }
    }
    if (number === 0 && order === 0) {
        answer = [0, 0];
    } else {
        answer = [number, order];
    }

    return answer;
}