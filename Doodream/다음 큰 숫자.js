function solution(n) {
    var nOneCount = findOneCount(n);
    var answer = 0;

    var nextN = n + 1;
    while (true) {
        if (findOneCount(nextN) === nOneCount) {
            answer = nextN;
            break;
        } else {
            nextN++;
        }
    }

    return answer;
}

function findOneCount(n) {
    var nBin = n.toString(2).split('');
    var nBinOneCount = 0;
    while (true) {
        var index = nBin.indexOf('1');
        if (index === -1) {
            break;
        } else {
            nBin.splice(index, 1);
            nBinOneCount++;
        }
    }

    return nBinOneCount;
}

var n = 15;
console.log(solution(n));