def odd_sum(n):
    return sum([i for i in range(n) if i % 2 != 0])


print(odd_sum(100))
