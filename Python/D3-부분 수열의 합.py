T = int(input())

for t in range(1, T+1):
    
    # N개의 자연수, 합이 K 이상
    N, K = list(map(int, input().split()))
    
    # 수열 A
    A = list(map(int, input().split()))
    
    # 합이 K인 총 개수
    cnt = 0
    
    # 비트마스킹을 이용한 부분집합
    for i in range(1<<N):
        
        # 합 초기화
        summ = 0
        
        for j in range(N):
            # 해당 비트가 부분집합으로 선택되었다면
            if(i & (1<<j)):
                # 합한다
                summ += A[j]
                
            # 합이 이미 K를 넘었다면 넘어간다
            if(summ > K):
                break
                
        # 합이 K 면 카운트
        if(summ == K):
            cnt += 1
    
    # 결과 출력
    print(f'#{t} {cnt}')