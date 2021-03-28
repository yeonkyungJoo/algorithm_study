function solution(numbers) {
    numbers = numbers.split('');
    const isPrime = (n) => {
        if (n <= 1) return false;
        if (n === 2 || n === 3) return true;
        if (n % 2 == 0) return false;
        var divider = 3;
        while (n / 2 > divider) {
            if (n % divider === 0) return false;
            divider += 2;
        }
        return true;
    }
    var pickNumberArr = [];
    const permutation = (arr, n, k) => {
        if (n === arr.length - 1) {
            const str = arr.slice(0, k).join("");
            if (!pickNumberArr.includes(str)) pickNumberArr.push(str);
            return;
        } else {
            for (let i = 0; i < arr.length; i++) {
                var tmp = arr[n];
                arr[n] = arr[i];
                arr[i] = tmp;

                permutation(arr, n + 1, k);
                arr[i] = arr[n];
                arr[n] = tmp;
            }
            return pickNumberArr;
        }
    };
    for (let k = 0; k < numbers.length; k++) {
        permutation(numbers, 0, k + 1);
    }
    var tmp = [];
    for (let i = 0; i < pickNumberArr.length; i++) {
        tmp[i] = Number(pickNumberArr[i]);
    }
    var set = new Set(tmp);
    pickNumberArr = [...set];
    //pickNumberArr.filter(n => isPrime(n) ? true : false);
    var answer = 0;
    pickNumberArr.forEach(n => {
        isPrime(n) ? answer++ : answer;
    })

    return answer;
}
var numbers = "17";
console.log(solution(numbers));