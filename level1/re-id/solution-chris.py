from math import sqrt


def isPrime(x):
    current = 2
    limit = int(sqrt(x))

    while limit >= current:
        if x % current == 0:
            return False
        current += 1

    return True


def solution(n):
    target = n + 5
    so_far = ""
    current = 2

    while target > len(so_far):
        if isPrime(current):
            so_far = so_far + str(current)
        current += 1

    return so_far[n:target]



