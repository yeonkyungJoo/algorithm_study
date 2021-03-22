def solution(skill, skill_trees):
    count = 0

    for skill_tree in skill_trees:
        i = 0
        for c in skill_tree:
            if c in skill:
                if skill[i] != c:
                    break
                else:
                    i += 1
        else:
            count += 1

    return count

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))