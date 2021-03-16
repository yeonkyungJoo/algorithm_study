function solution(s) {
  let compressedStringLengthArr = [];

  // i는 압축문자 단위가 s길이의 절반을 넘을수 없으므로 그만큼 반복한다.
  for (let i = 0; i < s.length / 2; i++) {
    let compressedStringLength = i + 1;
    let repeatStringCount = 1;
    let newString = "";

    // j는 압축문자가 다음문자와 같은지 s에 대해서 전부 비교해 나가본다.
    for (let j = 0; j < s.length; j += compressedStringLength) {
      let currentString = s.substring(j, j + compressedStringLength);
      let nextString = s.substring(
        j + compressedStringLength,
        j + 2 * compressedStringLength
      );

      //현재문자와 다음문자가 같다면 반복횟수 증가
      if (currentString === nextString) {
        repeatStringCount += 1;
        // 같지 않다면 더이상 반복이 안되는 것이므로 새로운 문자열에 반복횟숫를 넣어서 반복문자열을 넣는다.
      } else {
        if (repeatStringCount !== 1) {
          newString = newString + repeatStringCount + currentString;
          // 반복이 안된다면 현재 문자열이 나머지 문자열이 되므로 기존 문자열에 붙여 넣는 것이다.
        } else {
          newString = newString + currentString;
        }
        //반복 횟수 초기화
        repeatStringCount = 1;
      }
    }
    // 압축완료된 문자열 케이스 길이 하나 추가
    compressedStringLengthArr.push(newString.length);
  }

  var answer = Math.min(...compressedStringLengthArr);
  return answer;
}

console.log(solution("aabbaccc"));
