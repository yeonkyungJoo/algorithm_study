def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x * 5, reverse=True)
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    numbers = [0, 0, 0, 0]
    print(solution(numbers))