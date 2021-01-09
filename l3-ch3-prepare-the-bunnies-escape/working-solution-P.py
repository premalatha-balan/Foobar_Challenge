import numpy as np
import copy

def rm1wall(node,mmap):
    h,w = np.shape(mmap)
    ir, ic = node[0],node[1]
    if mmap[ir, ic]==1:
        nei_lst = nei(node, mmap)
        if len(nei_lst)>1: 
            mmap[ir,ic]=0
            print("removed wall at", node)
            return
    return


def nei(node, mmap):
    h,w = np.shape(mmap) 
    nei_lst=[]
    ir, ic = node[0], node[1]
    
    if ir-1>=0 and mmap[ir-1, ic] ==0: nei_lst.append([ir-1, ic]) #up
    if ir+1<h and mmap[ir+1, ic] ==0: nei_lst.append([ir+1, ic]) #down   
    if ic-1>=0 and mmap[ir, ic-1] ==0: nei_lst.append([ir, ic-1]) #left
    if ic+1<w and mmap[ir, ic+1] ==0: nei_lst.append([ir, ic+1]) #right  
    
    return nei_lst


def find_path(mmap):
    h,w = np.shape(mmap)
    # zeros = [(i,j) for i in range(h) for j in range(w) if mmap[i,j]==0]
    # print(zeros, "zeros")
    
    
    queue = [[[0,0]]]
    nb=0
    path=[]

    nodes=[[0,0]]

    for node in nodes:
        if node == [h-1,w-1]:
            print("I am at the end", node, "node", h-1, w-1)
            for i in queue:
                if [h-1,w-1] in i:
                    path.append(len(i))
            # print(queue, "queue")
            for branch in queue:
                print(branch)
                print(len(branch))
            print(path, "path")
            return path             

        # ir, ic = node[0],node[1]      

        for i in queue:
            if node in i:
                nb=queue.index(i)
                if nb == 1:
                    print(node, "node at index", nb )
                    print(i, "i - branch")
        
        x = nei(node,mmap)
        if [2,4] in x:
            print(node, "node for [2,4]")
            print(x, "neighbours")

        # if len(x)==1:
        #     if x[0] not in nodes: 
        #         nodes.append(x[0])
        #         queue[nb].append(x[0])
        #     elif x[0] in nodes: queue.pop(nb)
            
        # elif len(x)>1: #when uncommenting this, increase the tab for the following lines until appending queue[nb+i]
        
        if len(x)!=0:
            xt = copy.deepcopy(x)
            for i in xt:
                if i in nodes:
                    x.remove(i)
        
        if len(x)==0: 
            print(node, "node")
            print(queue[nb], "at index", nb)
            queue.pop(nb) # this is not an else statement for the above if
        elif len(x)==1:
            nodes.append(x[0])
            queue[nb].append(x[0])
        else:
            for i in x: nodes.append(i)
            if node == [2,3]:
                print(queue[nb], "branch for node [2,3] and index is", nb)
            xb = copy.deepcopy(queue[nb])
            for i in range(1,len(x)): queue.insert(nb+i, xb)    #the mistake was here
            for i in range(len(x)): 
                queue[nb+i].append(x[i])
                
    for i in queue:
        if [h-1,w-1] in i:
            path.append(len(i))
    # print(queue, "queue")
    for branch in queue:
        print(branch)
        print(len(branch))
    print(path)         
    return path


def solution(nmap):
    mmap = np.array(nmap)
    h,w = np.shape(mmap)
    print(h,w, "rows and columns")

    walls = [(i,j) for i in range(h) for j in range(w) if mmap[i,j]==1]

    
    paths =[]
    path = find_path(mmap)

    if len(path)!=0:
        if min(path)==h+w-1:
            return min(path)
           
    for wall in walls:
        rm1wall(wall,mmap)
        path = find_path(mmap)

        if len(path)!=0:
            if min(path)==h+w-1:
                return min(path)
            else:
                for p in path:
                    paths.append(p)
                if min(paths)==h+w-1:
                    return min(paths)
                else: 
                    return min(paths)
        mmap[wall[0], wall[1]] = 1     
        
        #print(path, "path")
    return min(paths)

# answer is 7
# nmap=[[0, 1, 1, 0],
#       [0, 0, 0, 1],
#       [0, 1, 0, 0], 
#       [0, 1, 1, 0]]

# answer is 11
# nmap = [[0, 0, 0, 0, 0, 0], 
#         [1, 1, 1, 1, 1, 0], 
#         [0, 0, 0, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 1, 1, 1, 1, 1], 
#         [0, 0, 0, 0, 0, 0]]

# # answer is 
# nmap =  [[0, 1, 0, 1, 0, 0, 0], 
#          [0, 0, 0, 1, 0, 1, 0]]

# #test case - answer is 15
# nmap = [[0, 0, 0, 1, 1,	0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 1, 0],
#         [0, 1, 1, 1, 1,	1, 0, 0, 1],
#         [0, 0, 0, 1, 1,	1, 0, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0, 1, 0]]

nmap = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(nmap))
