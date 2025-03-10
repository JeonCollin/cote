def permutation(idx):
    
    # nPr 순열 완성
    if(idx == R):
        print(P)
        
    # 순열 리스트 고르기
    else:
        for i in range(4):
            if(used[i] == 0):
                used[i] = 1
                P[idx] = mylist[i]
                permutation(idx+1)
                used[i] = 0
                
                
                
mylist = [1,2,3,4]
used = [0,0,0,0]
R = 2
P = [0]*R
PI = [0]*R

# permutation(0)

def nPIr(idx):
    # 중복순열
    
    # 중복순열 완성
    if(idx == R):
        print(PI)
        
    else:
        for i in range(4):
            PI[idx] = mylist[i]
            nPIr(idx+1)
        
nPIr(0)
        