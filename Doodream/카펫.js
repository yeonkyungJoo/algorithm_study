function solution(brown, yellow) {
    let totalBlock = brown + yellow;
    for (let a = 3; a < brown / 2 + 1; a++) {
        // a는 세로 b는 가로 
        if (totalBlock % a !== 0) {
            continue;
        }
        let b = ((brown - 2 * a + 4) / 2);
        if (b === totalBlock / a) {
            if (a >= b) {
                return [a, b];
            } else {
                return [b, a];
            }
        }
    }
}

