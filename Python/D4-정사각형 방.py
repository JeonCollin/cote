def push(item):
    global top

    top += 1

    # overflow
    if(top == N**2):
        pass

    # push
    else:
        stack[top] = item

def pop():
    global top

    # underflow
    if(top == -1):
        return False

    # pop
    else:
        top -= 1
        return stack[top+1]

def max_go(start):
    # 가려는 방향이 하나 밖에 없어서 굳이 DFS/BFS 안해도 될듯
    global rooms
    global visited

    # 상 하 좌 우 제자리
    drow = [-1, 1,  0, 0, 0]
    dcol = [ 0, 0, -1, 1, 0]

    # 움직임 횟수
    move = 1

    while True:

        # 현재 위치에서 갈 수 있는 위치 확인
        for i in range(5):
            row = start[0] + drow[i]
            col = start[1] + dcol[i]

            # 영역을 벗어나지 않고
            # 방 번호가 1 크다면
            if(0 <= row < N and 0 <= col < N
               and rooms[row][col] - rooms[start[0]][start[1]] == 1):
                
                # 가려는 방이 이미 갔었던 방이면 결과를 더하면 된다
                if(visited[row][col] != 0):
                    return move + visited[row][col]
                
                # 그게 아니라면 그 방으로 이동하고 움직임 갱신
                start[0] = row
                start[1] = col
                move += 1
            
        # 갈 수 있는 방이 없다면 지금까지의 결과 리턴
        if(row == start[0] and col == start[1]):
            return move

T = int(input())

for t in range(1, T+1):

    # 다음 N개의 줄
    N = int(input())

    # 스택 초기화
    stack = [0]*(N**2)
    top = -1

    # 2차원 방 받기
    # 자기 방보다 정확히 1이 커야 이동할 수 있다
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 방문했던 방은 최대 움직임 횟수를 기록
    visited = [[0]*N for _ in range(N)]
    max = 0

    for i in range(N):
        for j in range(N):
            # 현재 방에서 최대 움직임
            move = max_go([i, j])
            # 현재 방의 움직임 기록
            visited[i][j] = move

            # 최대값 갱신
            if(move >= max):
                max = move


    # 결과 출력
    print(f'#{t} {move}')