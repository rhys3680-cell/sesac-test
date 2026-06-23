def solution(n):
    total = 0
    for i in range(n):
        total += i
    return total


def solution2(n):
    li1 = []
    for i in range(n):
        li1.append(i)

    return sum(li1)


def solution3(n):
    return sum([i for i in range(n)])


print(solution(101))
