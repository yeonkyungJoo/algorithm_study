function solution(people, limit) {
    people.sort(function (a, b) { return a - b });
    for (var i = 0, j = people.length - 1; i < j; j--) {
        if (people[i] + people[j] <= limit) i++;
    }
    return people.length - i;
}

var people = [70, 50, 80, 50];
var limit = 100;

console.log(solution(people, limit));