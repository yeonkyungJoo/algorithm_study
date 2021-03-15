function solution(n) {
  let number = n;
  let answer = "";

  // number가 0일때 까지 반복
  while (number > 0) {
    // 맨 뒷 자리 숫자가 4인 경우는 3의 배수인 경우
    if (number % 3 === 0) {
      // 4 숫자를 추가
      answer = "4" + answer;
      // number를 3으로 나누고 1를 뺀다.
      number = number / 3 - 1;
      // 맨 뒷자리 숫자가 1인 경우는 3으로 나눈 나머지가 1인경우
    } else if (number % 3 === 1) {
      answer = "1" + answer;
      // 3으로 나누면 나머지가 생기므로 버린다.
      number = Math.floor(number / 3);
      // 1인 경우가 아니라면 자동으로 2
    } else {
      answer = "2" + answer;
      number = Math.floor(number / 3);
    }
  }
  return answer;
}

//pull req 확인 ?
