def is_prime(b):    
    for i in range(2,int(b**0.5)+1):
        if b%i==0: return False
    return True

def build_prime_str(n):
    pstr = "23"
    
    b=4
    while len(pstr)<=n+5:
        b+=1
        if is_prime(b): pstr += str(b)  
        # print(pstr, b)
    return pstr


def solution(n):
    pstr= build_prime_str(n)
    # print(pstr)
    
    return pstr[n:n+5]
    
