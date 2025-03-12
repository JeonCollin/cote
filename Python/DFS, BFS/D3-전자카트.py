def permutation(idx):
    global used
    global minn
    global mylist
    
    if(idx == N-1):
        # 순열 완성
        # print(P)
        sumn = mylist[0][P[0]]
        now = P[0]
        
        # 합 구하기
        for j in range(1, N):
            # j번 > P[j]번
            # P[j] >> P[P[j]]
            sumn += mylist[now][P[j]]
            now = P[j]
        
        # 최소값 갱신
        if(sumn < minn):
            minn = sumn
        
    else:
        # 순열을 만드는 과정
        # 순열의 마지막은 무조건 0이다
        for i in range(1, N):
            # 만약 지금 원소를 선택하지 않았었다면
            if(used[i] == 0):
                # 선택한다
                used[i] = 1
                P[idx] = index[i]
                permutation(idx+1)
                # 다시 선택 해제
                used[i] = 0
    


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    # 인덱스 리스트 만들기
    index = [i for i in range(N)]
    used = [0]*N
    P = [0]*N
    
    mylist = [list(map(int,input().split())) for _ in range(N)]
    
    # 최소값 초기화
    minn = 100*N
    
    permutation(0)
    
    # 결과출력
    print(f'#{t} {minn}')