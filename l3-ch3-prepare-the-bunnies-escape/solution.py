import numpy as np

def rm_1(mmap,iw,jw):
    h, l = np.shape(mmap)
    if iw==h and jw==l:
        return iw, jw      
   
    for i in range(iw,h):
        for j in range(l):
            if i==iw and j<=jw:
                continue
            elif mmap[i,j]==1:
                    if (j-1>=0 and mmap[i,j-1]==0) and (j+1<l and mmap[i,j+1]==0): 
                        mmap[i,j] = 0  # left and right
                        return i, j
                    if (i-1>=0 and mmap[i-1,j]==0) and (i+1<h and mmap[i+1,j]==0): 
                        mmap[i,j] = 0  # up and down
                        return i, j
                    if (i-1>=0 and mmap[i-1,j]==0) and (j-1>=0 and mmap[i,j-1]==0): 
                        mmap[i,j] = 0  # up and left
                        return i, j
                    if (i-1>=0 and mmap[i-1,j]==0) and (j+1<l and mmap[i,j+1]==0): 
                        mmap[i,j] = 0  # up and right
                        return i, j
                    if (i+1<h and mmap[i-1,j]==0) and (j-1>=0 and mmap[i,j-1]==0): 
                        mmap[i,j] = 0  # down and left
                        return i, j
                    if (i+1<h and mmap[i-1,j]==0) and (j+1<l and mmap[i,j+1]==0): 
                        mmap[i,j] = 0  # down and right
                        return i, j

                       
    return i,j

def get_box(loc,mmap):
    h, l = np.shape(mmap)
    ir, ic=loc[0],loc[1]
    box=[[ir,ic]]   
    
    if ic-1>=0 and mmap[ir,ic-1]==0:  #left
        box.append([ir, ic-1])
    if ic+1<l and  mmap[ir,ic+1]==0: #right
        box.append([ir, ic+1])
    if ir-1>=0 and mmap[ir-1,ic]==0: #up
        box.append([ir-1, ic])    
    if ir+1<h and mmap[ir+1,ic]==0: #down
        box.append([ir+1, ic])
        
    return box

def matching(mmap):
    h, l = np.shape(mmap)
        
    count=0
    biglst=[]

    src=[0,0]
    src_box=[src]
    dest=[h-1,l-1]
    dest_box=[dest]
    
    nzcount=np.count_nonzero(mmap)
    zcount=h*l-nzcount

    b=0
    while b<zcount:
        b+=1

        move_src=[]
        count+=1
        for src in src_box:
            if src not in biglst:
                temp=get_box(src, mmap)
                biglst.append(src)
                for k in temp:
                    if k not in move_src: move_src.append(k)
            elif src not in move_src: move_src.append(src)
        
        for k in move_src:
            if k in dest_box:
                count+=1
                if k not in biglst: biglst.append(k)
                return count
        #swap
        if len(move_src)>len(dest_box):
            src_box=[]
            for k in dest_box:
                src_box.append(k)
            dest_box=[]
            for k in move_src:
                dest_box.append(k)
        else:
            src_box=[]
            for k in move_src:
                src_box.append(k) 
               
    return count


def solution(nmap):
    mmap = np.array(nmap)
    h, l = np.shape(mmap)
    if h==2 and l==2:
        return 3

    count=0
    countlst=[]
    
    loopcoount=np.count_nonzero(mmap)
    if loopcoount==0:
        return h+l-1
    
    count = matching(mmap)
    if count==h+l-1:  
        return count
    if count not in countlst and count!=0 : countlst.append(count)
    iw,jw=0,0

    b=0
    while b<loopcoount:
        b+=1

        iw, jw = rm_1(mmap, iw, jw)
        count = matching(mmap)
        if count==h+l-1:  
            return count
        if count not in countlst: countlst.append(count)
        mmap[iw,jw]=1
   
    return min(countlst)
