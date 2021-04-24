def solution(numbers, target):
    count = 0
    prev = [numbers[0], -numbers[0]]
    
    for i in range(1, len(numbers)):
        next_number = numbers[i]
        _next = []
        for num in prev:
            _next.append(num + next_number)
        prev = _next
        
    for number in prev:
        if number == target:
            count += 1
    return count
