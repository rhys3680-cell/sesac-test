def solution1(numbers):
    return len(x for x in range(1, numbers + 1) if x % 2 == 0)


def cnt_even2(n):
    return sum(1 for i in range(1, n + 1) if i % 2 == 0)


# int 1, 2, 3
# float 8bit / .0124942
# double 16bit
# 문자열 -> string -> tuple
# list ->
# tuple ->
# dict ->
# Counter
