function solution(relation) {
    let answer = 0;
    let attrNum = relation[0].length;
    let combList = [];
    let keyList = [];

    for (let i = 1; i <= attrNum; i++) {
        comb(combList, [], 0, attrNum, i, 0);
    }

    for (let i = 0; i < combList.length; i++) {
        addKey(keyList, combList[i], relation);
    }
    console.log(keyList);
    return keyList.length;
}
function addKey(keyList, key, relation) {

    let isMin = true;
    for (let i = 0; i < keyList.length; i++) {
        let prevKey = keyList[i];
        for (let j = 0; j < key.length; j++) {
            prevKey = prevKey.filter(ele => ele !== key[j]);
        }
        if (prevKey.length === 0) {
            isMin = false;
        }
    }

    if (keyList.length !== 0 && !isMin) {
        return;
    }
    let arr = [];
    let isUnique = true;

    for (let i = 0; i < relation.length; i++) {
        let findEle = arr.find(ele => {
            let flag = true;
            for (let j = 0; j < key.length; j++) {
                if (ele[key[j]] !== relation[i][key[j]])
                    flag = false;
            }
            return flag;
        })
        if (findEle !== undefined) {
            isUnique = false;
        } else {
            arr.push(relation[i]);
        }
    }

    if (isUnique) {
        keyList.push(key);
    }

}

function comb(list, arr, idx, n, r, target) {
    if (r === 0) {
        list.push(Object.assign([], arr));
    } else if (target === n) {
        return;
    } else {
        arr[idx] = target;
        comb(list, arr, idx + 1, n, r - 1, target + 1);
        comb(list, arr, idx, n, r, target + 1);
    }
}