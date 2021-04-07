function solution(cacheSize, cities) {
    var cache = [];
    var runTime = 0;
    cities = cities.map(x => x.toUpperCase())

    for (let i = 0; i < cities.length; i++) {
        var city = { name: cities[i], index: i };
        var isHit = cache.find(a => a.name === cities[i]);

        if (isHit) {
            var findIndex = cache.indexOf(isHit);
            cache[findIndex].index = i;
            runTime += 1;
        } else {

            cache.push(city);
            runTime += 5;
            if (cache.length > cacheSize) {
                cache.shift();
            }
        };

        cache.sort((a, b) => a.index - b.index);


    }

    var answer = runTime;
    return answer;
}

var cacheSize = 3;
var cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
console.log(solution(cacheSize, cities));
