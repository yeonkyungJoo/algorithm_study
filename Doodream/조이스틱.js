function basicformat(n) {
    let result = [];
    for (let i = 0; i < n; i++) {
        result.push("A");
    }
    return result;
}
function alphaMove(letter) {
    if (!letter) {
        return;
    }
    let index = letter.charCodeAt() - 64; //아스키코드 값으로 바꾼다/ A = 1, Z = 26
    //A -> Z 로 가는게 빠를지 Z -> A로 가는 게 빠를지 어떻게 판단하면 될까?
    if (index > 13) {
        return 26 - index + 1
    } else {
        return index - 1;
    }
}

//가장 가까운 a값을 찾는 것..
function leftright(name, index) {
    let left = 1;
    let right = 1;
    let rightIndex = index;
    let leftIndex = index;
    while (true) {
        rightIndex++;
        if (rightIndex === name.length) {
            rightIndex = 0;
        }
        if (name[rightIndex] !== 'A') {
            break;
        }
        else {
            right++;
        }
    }
    while (true) {
        leftIndex--;
        if (leftIndex < 0) {
            leftIndex = name.length - 1;
        }
        if (name[leftIndex] !== 'A') {
            break;
        }
        else {
            left++;
        }
    }
    if (left === right) {
        return [right, rightIndex];
    }
    return left > right ? [right, rightIndex] : [left, leftIndex];
}

function solution(name) {
    //A초기상태를 먼저 가져온다..
    let basic = basicformat(name.length);
    let result = 0; //결과값 넣을 곳
    //복사한 name 값을 만든다
    let cpname = name;
    //가장 가까운 a 값을 찾는다...
    let updown = name.split("").map(element => alphaMove(element))
    updown = updown.reduce((acc, cur) => (acc + cur), 0);
    //while 문을 돌린다. cpname 을 전부 AAAAA로 바꿀떄까지 맞춘다
    cpname = cpname.split("");
    cpname[0] = "A";
    let nowindex = 0;
    while (cpname.join("") !== basic.join("")) {
        //방향설정을 먼저한다.
        let [count, index] = leftright(cpname, nowindex);
        result += count;
        cpname[index] = 'A';
        nowindex = index;
    }
    return result + updown;
}