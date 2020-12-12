import numpy as np

def get_box(src):
    
    loc=np.where(floor==src)
    r,c=str(loc[0]),str(loc[1])
    ir,ic=int(r[1]),int(c[1])
    
    if ir-2<=0:
        irs=0
    else:
        irs=ir-2
        
    if ic-2<=0:
        ics=0
    else:
        ics=ic-2
    
    box = floor[irs:ir+3,ics:ic+3 ]

    return box

def get_moved(src):
    box=get_box(src)
    moved=[]
    for i in move_lst:
        check=src+i
        if check>=0 and check<=63:
            if check in box:
                moved.append(check)
    return moved

def solution(src, dest):
    if(src==dest):
        return 0
    move1=[]
    moveup1=[]
    count=0
    NotSolved=True
   
    b=0
    move1=[src]
    moveup1=[dest]
    while NotSolved and b<100:
        b+=1
        move_src=[]
        
        for j in move1:
            moved=get_moved(j)
            for k in moved:
                if k in moveup1:
                    count+=1
                    NotSolved=False
                    return count
                else:
                    if (k>=0 and k<=63) and k not in move_src:
                        move_src.append(k)

        if len(move_src)!=0:
            count+=1
        else:
            print("Not solved", NotSolved)
            return count
        
        move1=[]
        if(len(move_src)<=len(moveup1)): #swapping to start the search with the smaller list
            for i in move_src:
                move1.append(i)
        else:
            for i in moveup1:
                move1.append(i)
            moveup1=[]
            for i in move_src:
                moveup1.append(i)         

    return count


move_lst=[-17,-15,-10,-6,6,10,15,17]

floor = np.array([[0]*8]*8)

count=0
for j in range(8):
    for i in range(8):
        floor[j,i] = count
        count+=1


#running a solution
src=63
dest=0

no_moves=solution(src,dest)
print("no of moves needed to move from", src, "to", dest,"is", no_moves) #answer is 6
