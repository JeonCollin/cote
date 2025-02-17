def push(item_row, item_col):
    
    global top
    # 일단 top 증가
    top += 1

    # 오버플로우
    if(top == N**2):
        print('overflow')

    # push
    else:
        stack[top] = [item_row, item_col]

def pop():

    global top

    # underflow
    if(top == -1):
        return False

    # pop
    else:
        top -= 1
        return stack[top+1]

def find_way(arr, S, E):
    # S:시작, E:끝
    global N
    
    # 방문리스트 만들기
    visited = [[0]*N for _ in range(N)]

    # 상 하 좌 우
    drow = [-1, 1,  0, 0]
    dcol = [ 0, 0, -1, 1]

    # DFS
    while True:
        #print('a', S)
        # 방문 표기
        if(visited[S[0]][S[1]] == 0):
            visited[S[0]][S[1]] = 1 

        # 1단계: 방향 설정하기
        for i in range(4):
            ROW = S[0] + drow[i]
            COL = S[1] + dcol[i]

            # 미로 범위를 벗어나지 않도록 제한
            if(0 <= ROW < N and 0 <= COL < N):

                # 주변이 0이라면 갈 수 있는 곳
                # 방문한 적이 없다면 갈 수 있는 곳
                if((arr[ROW][COL] == 0 or arr[ROW][COL] == 3) and
                    visited[ROW][COL] == 0):
                    # 방문 표기
                    visited[ROW][COL] = 1
                    # 스택에 저장
                    push(S[0], S[1])
                    # 새로운 노드로 이동
                    S[0] = ROW
                    S[1] = COL
                    #print('b', S)

                    # 끝지점이라면 성공
                    if(S == E):
                        return 1
                    
                    break
        
        # 갈 수 없는 곳을 만났다면 pop
        else:
            #print('c', S)
            S = pop()
            #print('d', S)

            # 만약 underflow라면 실패
            if(S == False):
                return 0

                


T = int(input())

for t in range(1, T+1):

    # N: 미로크기
    N = int(input())

    # 스택 초기화
    # row, col 형태로 되어있는 2차원 원소를 가짐
    stack = [0]*(N**2)
    top = -1

    # 미로 받기
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점과 끝점 찾기
    for i in range(N):
        for j in range(N):
            if(maze[i][j] == 2):
                start = [i, j]

            if(maze[i][j] == 3):
                end = [i, j]

    # 결과출력
    print(f'#{t} {find_way(maze, start, end)}')