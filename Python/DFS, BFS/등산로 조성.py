'''
- 가장 높은 봉우리에서 시작
- 높은 곳에서 낮은 곳으로 이동 가능(같은 높이는 불가능)
- 원하는 만큼 깎을 수 있다
- 지형을 1보다 작게 하는 것도 가능
- 등산로의 최대 길이 구하기

# 아이디어
- BFS로 간다
- 본인 지역보다 크거나 같은 지역이 나오면 최초로 한 번 깎는다
- 그 이후로는 작은 것만 찾는다
'''
# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def DFS(start_row, start_col, height, move, use_K):
    # 좌표1, 좌표2, 현재의 높이(공사 감안), 움직임 횟수, 공사 기록
    global maps
    global K
    global maxx
    global visited
    
    # 방문 기록
    move = move + 1
    visited[start_row][start_col] = move
    # 최대 움직임 갱신
    if(maxx < move):
        maxx = move
    
    # 인접 지역 탐색
    for i in range(4):
        ROW = start_row + drow[i]
        COL = start_col + dcol[i]
        
        # 범위를 벗어나지 않는 지 확인
        # 어차피 갔던 곳을 돌아가면 최장거리에 포함 안됨
        if(0 <= ROW < N and 0 <= COL < N
           and visited[ROW][COL] == 0):
            
            # 우선 차이를 구한다
            diff = maps[ROW][COL] - height
            
            # 가려는 곳이 자기보다 작다면 갈 수 있다
            if(diff < 0):
                DFS(ROW, COL, maps[ROW][COL], move, use_K)
                # 원상복구
                visited[ROW][COL] = 0
                
            # 가려는 곳이 자기보다 크거나 같은 경우
            # 공사한 적이 없고
            # 공사 높이보다 작으면 갈 수 있다
            elif(use_K == False and 0 <= diff < K):
                # 공사 진행 >> 진행 후 높이 주기
                after_height = maps[ROW][COL] - diff - 1
                DFS(ROW, COL, after_height, move, True)
                visited[ROW][COL] = 0



T = int(input())

for t in range(1, T+1):
    
    # N x N, 공사 가능 깊이 K
    N, K = list(map(int, input().split()))
    
    # 지도 정보
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    max_height = 0
    top_list = []
    # 최댓값
    maxx = 0
    
    # 최대 봉우리들 찾기
    for i in range(N):
        for j in range(N):
            if(maps[i][j] >= max_height):
                max_height = maps[i][j]
                
    for i in range(N):
        for j in range(N):
            if(maps[i][j] == max_height):
                top_list.append([i, j])
    
    
    
    # 최대 봉우리에서 떨어지기
    for i in range(len(top_list)):
        # 방문 리스트 생성
        visited = [[0]*N for _ in range(N)]
        x = top_list[i][0]
        y = top_list[i][1]
        DFS(x, y, maps[x][y], 0, False) # False: 아직 공사 안함
        
        # for j in range(N):
        #     print(visited[j])
        # print()
        
        # for j in range(N):
        #     print(maps[j])
        # print()
        
        # 방문리스트에서 최대 횟수 찾기
    
    
    
    # 결과 출력
    print(f'#{t} {maxx}')
