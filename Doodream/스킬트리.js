function solution(skill, skill_trees) {
    var answer = 0;
    var skillArr = skill.split('');

    skill_trees.map(x => {
        var isIncludesAny = false;
        for (let i = 0; i < skillArr.length; i++) {
            var isIncludes = x.indexOf(skillArr[i]);
            if (isIncludes !== -1) {
                isIncludesAny = true;
                if (i === 0) {
                    continue;
                } else {
                    var isIncludesPreskill = x.indexOf(skillArr[i - 1]);
                    if (isIncludesPreskill === -1) {
                        return;
                    }
                    if (isIncludesPreskill > isIncludes) {
                        return;
                    }
                }
            }
        }
        if (isIncludesAny === false) {
            answer++;
            return
        }
        answer++;
    })
    return answer;
}

let skill = "CBDK";
let skill_trees = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"];

console.log(solution(skill, skill_trees));