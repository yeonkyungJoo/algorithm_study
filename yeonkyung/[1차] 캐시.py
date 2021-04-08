def solution(cacheSize, cities):
    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    hit = 0
    miss = 0
    for city in cities:
        if city.upper() in cache:
            hit += 1
            cache.pop(cache.index(city.upper()))
            cache.append(city.upper())
        else:
            miss += 1

            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city.upper())

    return hit * 1 + miss * 5

if __name__ == "__main__":
    cacheSize = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    print(solution(cacheSize, cities))