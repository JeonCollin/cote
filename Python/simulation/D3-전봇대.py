T = int(input())

for t in range(1, T+1):
    
    # N: 전선의 개수
    N = int(input())
    
    mylist = [[0]*2 for _ in range(N)]
    
    for n in range(N):
        # 시작점, 끝점 받기
        s, e = list(map(int, input().split()))
        
        mylist[n][0] = [s]
        mylist[n][1] = [e]
        
    # 교점의 개수: 시작점 < 다른전선 시작점 and 다른전선 끝점 < 끝점
    cnt = 0
    for n in range(N):
        
        start = mylist[n][0]
        end = mylist[n][1]
        
        # 다른 전선과 비교한다
        for i in range(N):
            # 지금 지점은 비교할 필요 없다
            if(i == n):
                continue
            
            another_start = mylist[i][0]
            another_end = mylist[i][1]
            
            if(start < another_start and another_end < end):
                cnt += 1
    
    print(f'#{t} {cnt}')