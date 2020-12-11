from itertools import combinations

def solution(L):
    
    numstr=""
    
    L.sort(reverse=True)
    
    for i in range(len(L)+1,1,-1):
        for lstup in combinations(L,i):
            if sum(lstup)%3 == 0:
                for i in lstup:
                    strtup=str(i)
                    numstr+=strtup
                
                return int(numstr)
   
    return 0


L=[3, 1, 4, 1, 5, 9]  #answer = 94311
#L=[1,1,1,1,1]
print(solution(L))
