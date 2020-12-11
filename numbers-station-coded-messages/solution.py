def solution(l,t):
    print(l, t)
    for i in range(len(l)-1):
        for j in range(i,len(l)+1):
            l1=l[i:j]
            print(l1, sum(l1),t, i,j)
            if sum(l1)==t:
                print(l1, sum(l1), t, i, j-1)
                return i, j-1
            elif sum(l1)>t:
                break

    return [-1, -1]

"""
l = [1, 2, 3, 4]
t=15
#[-1,-1]

l=[4, 3, 10, 2, 8] 
t=12
#[2,3]
print(solution(l,t))


l=[4, 3, 5, 7, 8]
t=12
#[0, 2]
print(solution(l,t))
"""

l=[1, 2, 3, 4]
t=15
#[-1, -1]
print(solution(l,t))
