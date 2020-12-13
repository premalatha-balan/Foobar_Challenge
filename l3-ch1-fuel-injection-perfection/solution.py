def solution(n):
    nn=int(n)
    if nn==1:
        return 0
    if nn==3:
        return 2
    if nn%2==0:
        return solution(nn/2)+1
    return solution((nn+nn%4 -2)/4)+3

#Example
n="6"
print(solution(n))

#Code solved by https://github.com/wandering-kiwi 
