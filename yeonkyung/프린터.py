def solution(priorities, location):
    queue = []
    count = 0
    for i, priority in enumerate(priorities):
        queue.append((i, priority))

    while queue:
        max_priority = max(queue, key=lambda x:x[1])[1]
        x = queue.pop(0)
        if x[1] != max_priority:
            queue.append(x)
        else:
            count += 1
            if x[0] == location:
                return count

if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))