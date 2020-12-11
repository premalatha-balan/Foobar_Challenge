def solution(l, t):
    for i in range(len(l)-1):
        for j in range(i,len(l)+1):
            l1=l[i:j]
            if sum(l1)==t:
                return [i, j-1]
            elif sum(l1)>t:
                break
    return [-1, -1]
