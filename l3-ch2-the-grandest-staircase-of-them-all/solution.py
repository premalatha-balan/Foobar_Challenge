def solution(n):
    if n <3 or n> 200:
        return 0
    ns = 1

    base_case = {1: [[]],
                  2: [[]],
                  3: [[2,1]],
                  4: [[3,1]],
                  5: [[4,1], [3,2]]
                  } 
       
    print("it is ok")  
    
    
    
    
    if n in base_case:
        print(len(base_case[n]))
    else:
        print("it is not in the base case yet")
        return 0
    
    
    
    
    ns = len(base_case[n])
    
    return ns

n= 6
print(solution(n))
