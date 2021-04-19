function solution(clothes) {
    const clothesCount = new Map();
    // clothes 배열을 받은 다음 clothesType목록만 추가 시킴
    for (let i = 0; i < clothes.length; i++) {
        // 만약 옷 종류가 등록 되지 않았다면 [옷 종류,  1] 추가
        if (!clothesCount.has(clothes[i][1])) clothesCount.set(clothes[i][1], 1);
        else {
            // 만약 옷 종류가 등록이 되어 있는 경우라면 [옷 종류 ,기존에 들어 있던 옷 종류의 갯수  + 1] 로 map 최신화
            clothesCount.set(clothes[i][1], clothesCount.get(clothes[i][1]) + 1);
        }
    }

    let answer = 1;
    const clothesIter = clothesCount.values();
    for (let i = 0; i < clothesCount.size; i++) {
        answer *= (clothesIter.next().value + 1);
    }
    return answer - 1;
}