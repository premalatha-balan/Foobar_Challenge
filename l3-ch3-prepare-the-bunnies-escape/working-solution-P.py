# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:12:50 2020

@author: Balan
"""
import numpy as np
import copy

def rm1wall(wall,mmap):
    h,w = np.shape(mmap)
    ir, ic = wall[0],wall[1]
    if mmap[ir, ic]==1:
        nei_lst = nei(wall, mmap)
        if len(nei_lst)>1: 
            mmap[ir,ic]=0
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
    
    queue = [[[0,0]]]
    nb=0
    path=[]

    nodes=[[0,0]]

    for node in nodes:
        if node == [h-1,w-1]:
            for i in queue:
                if [h-1,w-1] in i:
                    path.append(len(i))
            return path                  

        for i in queue:
            if node in i:
                nb=queue.index(i)

        x = nei(node,mmap)
       
        if len(x)!=0:
            xt = copy.deepcopy(x)
            for i in xt: 
                if i in nodes: x.remove(i)
        
        if len(x)==0: queue.pop(nb) 
        elif len(x)==1:
            nodes.append(x[0])
            queue[nb].append(x[0])
        else:
            for i in x: nodes.append(i)
            xb = copy.deepcopy(queue[nb])
            for i in range(1,len(x)): queue.insert(nb+i, xb) 
            for i in range(len(x)): queue[nb+i].append(x[i])
                
    for i in queue:
        if [h-1,w-1] in i: path.append(len(i))
              
    return path


def solution(nmap):
    mmap = np.array(nmap)
    h,w = np.shape(mmap)

    walls = [[i,j] for i in range(h) for j in range(w) if mmap[i,j]==1]
    
    paths =[]
    path = find_path(mmap)

    if len(path)!=0:
        if min(path)==h+w-1:
            return min(path)
    
    for wall in walls:
        rm1wall(wall,mmap)
        path = find_path(mmap)

        if len(path)!=0:
            if min(path)==h+w-1: return min(path)
            else:
                for p in path: paths.append(p)
                if min(paths)==h+w-1: return min(paths)
                
        mmap[wall[0], wall[1]] = 1     
        
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

# # answer is 10
nmap =  [[0, 1, 0, 1, 0, 0, 0], 
          [0, 0, 0, 1, 0, 1, 0]]

# #test case - answer is 15
# nmap = [[0, 0, 0, 1, 1, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 1, 0],
#         [0, 1, 1, 1, 1, 1, 0, 0, 1],
#         [0, 0, 0, 1, 1, 1, 0, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0, 1, 0]]

# #test case - answer is 15
# nmap = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 1, 1, 0, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 1, 0],
#         [0, 1, 1, 1, 1, 1, 0, 0, 1],
#         [0, 0, 0, 1, 1, 1, 0, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0, 1, 0]]

# nmap = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(solution(nmap))
