
def solution(i):
    primes = ""
    n=1
    while len(primes) <= i+5:
        n += 1
        if all(n % m for m in range(2, int(n**0.5) +1)): primes += str(n)
    
    return primes[i:i+5]


print(solution(10))
