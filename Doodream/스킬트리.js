function solution(skill, skill_trees) {
    var answer = 0;
    var skillArr = skill.split('');

    skill_trees.map(x => {
        var skillIndex = [];
        var next = false;
        var isIncludesAny = false;

        for (let i = 0; i < skillArr.length; i++) {
            var isIncludes = x.indexOf(skillArr[i]);
            if (isIncludes !== -1) {
                isIncludesAny = true;
                if (i === 0) {
                    skillIndex.push(isIncludes);
                    continue;
                }
                if (i > 0) {
                    if (x.indexOf(skillArr[i - 1]) !== -1) {
                        skillIndex.push(isIncludes);
                    } else {
                        next = true;
                        break;
                    }
                }
            }
        }
        if (isIncludesAny === false && skillIndex.length === 0) {
            //console.log(x);
            answer++;
            return
        }

        if (!next) {
            var notSortSkillIndex = skillIndex.slice();
            skillIndex.sort();
            if (notSortSkillIndex.join('') === skillIndex.join('')) {
                //console.log(x);
                answer++;
                return
            }
        }

    })

    return answer;
}

let skill = "CBDK";
let skill_trees = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"];

console.log(solution(skill, skill_trees));