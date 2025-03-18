'''
최초힙: 생산비용이 최소인 쪽으로 우선 탐색
'''

def backtracking(idx):
    global minn
    global summ
    
    # 공장을 선택하는 중에 이미 최솟값보다 크다면 리턴
    if(summ >= minn):
        return
    
    # 모든 공장을 선택했으면
    if(idx == N):
        # 최솟값 갱신
        if(minn > summ):
            minn = summ
    
    for i in range(N):
        # 사용한 적 없는 인덱스는 사용 가능
        if(used[i] == 0):
            used[i] = 1
            summ += volumes[idx][i]
            backtracking(idx+1)
            # 사용기록 초기화
            used[i] = 0
            summ -= volumes[idx][i]
            


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    # N x N 배열
    volumes = [list(map(int, input().split())) for _ in range(N)]   
    
    # 최소값, 합 초기화
    minn = 99*N
    summ = 0
    # 사용인덱스 초기화
    used = [0]*N
    
    backtracking(0)
    
    # 결과 출력
    print(f'#{t} {minn}')