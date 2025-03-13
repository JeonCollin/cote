
T = int(input())

for t in range(1, T+1):
    
    # N 신청서 개수
    N = int(input())
    
    # 작업시간 리스트 생성
    work_list = []
    
    for n in range(N):
        # s 화물차의 작업 시작 시간, e 종료시간
        s, e = list(map(int, input().split()))
        work_list.append([s,e])
        
    # 종료와 동시에 작업 시작할 수 있다
    # 시작: 포함 >> 종료: 포함x
    
    # 종료시간 기준으로 오름차순 정렬
    # i가 오른쪽에서 출발
    for i in range(N-1, 0, -1):
        # j가 왼쪽에서 출발
        for j in range(0, i):
            # 왼쪽이 더 크다면 스왑
            if(work_list[j][1] > work_list[i][1]):
                work_list[j], work_list[i] = work_list[i], work_list[j]
                
    # 가장 처음 시작하는 것부터 시작한다
    # 종료 시간 이후 바로 시작할 수 있는 것부터 시작한다
    work_cnt = 1
    idx = 1
    start = work_list[0][0]
    end = work_list[0][1]
    
    while(idx < N):

        # 지금 시작하는 작업이 이전 종료시간보다 크거나 같다면 작업 가능
        if(end <= work_list[idx][0]):
            work_cnt += 1
            
            # 이 작업을 기준으로 옮긴다
            start = work_list[idx][0]
            end = work_list[idx][1]
        
        idx += 1
        
    # 결과 출력
    print(f'#{t} {work_cnt}')
        