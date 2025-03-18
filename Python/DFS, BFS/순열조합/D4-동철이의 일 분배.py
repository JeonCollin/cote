def backtracking(idx):
    global maxx
    global mul
    
    # 만약 지금 곱하는 수가 이미 지금보다 작다면
    # 확률을 곱하면 작아지니까 가능성이 없다
    if(mul <= maxx):
        return
    
    # 모든 케이스를 검사했다면
    if(idx == N):
        # 최대값 갱신
        if(mul > maxx):
            maxx = mul
        
    else:
        for i in range(N):
            # 일하지 않은 직원이라면 일해라
            if(used[i] == 0):
                
                # 곱할 수가 0이라면 넘어간다
                if(works[idx][i] == 0):
                    continue
                
                used[i] = 1
                mul *= works[idx][i]/100
                backtracking(idx+1)
                used[i] = 0
                mul = mul / (works[idx][i]/100)
        

T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    # 일 잘할 확률
    works = [list(map(int, input().split())) for _ in range(N)]
    
    # 사용리스트 생성
    used = [0]*N
    
    # 최대, 곱 초기화
    maxx = 0
    mul = 1
    
    backtracking(0)
    
    # 소수점 6자리까지로 바꾼다
    maxx = maxx*100
    result = round(maxx, 6)
    
    # 결과 출력
    print(f'#{t}',format(result, '.6f'))