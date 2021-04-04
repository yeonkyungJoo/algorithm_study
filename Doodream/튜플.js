function solution(s) {
    var answer = [];
    var sTmp = JSON.parse(JSON.stringify(s));
    sTmp = sTmp.split(",{").join('');
    sTmp = sTmp.split("}");
    sTmp[0] = sTmp[0].split("{").join('');
    sTmp = sTmp.filter(a => a.length > 0);
    sTmp = sTmp.map(a => a.split(","));
    sTmp.sort((a, b) => a.length - b.length);
    sTmp.map(x => {
        if (answer.length === 0) answer.push(...x);
        x.map(y => {
            if (!answer.includes(y)) {
                answer.push(y);
            }
        })
    });
    answer = answer.map(Number);
    return answer
}

var s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
console.log(solution(s));