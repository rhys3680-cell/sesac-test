def solution(numbers):
    li1 = []
    count = 0
    for x in range(numbers):
        if x % 2 == 0:
            li1.append(x)
            count += 1

    print(li1)
    return count


print(solution(101))

print(0 % 2 == 0)


def cnt_even(n):
    return sum(1 for i in range(1, n + 1) if i % 2 == 0)
