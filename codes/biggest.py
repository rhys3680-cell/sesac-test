import random
# from collections import Counter

li1 = []

for i in range(101):
    li1.append(random.randint(1, 1000))

# print(max(li1))


def solution(numbers):
    biggest = numbers[0]  # 일단 첫 값을 후보로
    # second = numbers[1]
    # print(numbers)
    for x in numbers[2:]:
        if x > biggest:  # 더 크면 후보 교체
            biggest = x
        # print(biggest, x)
    return biggest


print(solution(li1))

# counter = Counter(li1)

# print(counter)
