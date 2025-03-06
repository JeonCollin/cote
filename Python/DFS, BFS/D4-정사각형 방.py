# 상 하 좌 우
drow = [-1, 1,  0, 0]
dcol = [ 0, 0, -1, 1]

# def push(item):
#     global top

#     top += 1

#     # overflow
#     if(top == N**2):
#         pass

#     # push
#     else:
#         stack[top] = item

# def pop():
#     global top

#     # underflow
#     if(top == -1):
#         return False

#     # pop
#     else:
#         top -= 1
#         return stack[top+1]

def DFS(rooms, start):
    global N
    visited = [[0]*N for _ in range(N)]

    # 이동 횟수: 본인 방 포함
    move = 1

    while True:
        # 방문기록 먼저
        if(visited[start[0]][start[1]] == 0):
            visited[start[0]][start[1]] = 1

        # 상하좌우로 갈 수 있는 곳을 확인한다
        for i in range(4):
            Row = start[0] + drow[i]
            Col = start[1] + dcol[i]

            # 영역을 벗어나지 않도록 제한
            # 차이가 1이라면 갈 수 있는 방이다
            # 방문한 적이 없다면 갈 수 있는 방이다
            if(0 <= Row < N and 0 <= Col < N
               and rooms[Row][Col] - rooms[start[0]][start[1]] == 1):
                # 이전 위치 push
                # stack.append(start)
                #push(start)
                # 위치 갱신
                start[0] = Row
                start[1] = Col
                move += 1
                break

        # 갈 수 있는 곳이 없을 경우 되돌아가자
        # 근데 이 문제에서는 되돌아가는게 의미 없다.
        else:
            return move
            # start = pop()

            # # 갈 수 있는 모든 곳을 갔다면 끝났다
            # if(start == False):
            #     return move


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

    # 움직임 최대값 초기화
    max = 1
    # 최대값의 방의 최소 번호
    min_room = N**2

    # 2차원을 순회하며 시작점을 정하자
    # 근데 무식하게 순회하면 시간초과 나옴
    for row in range(N):
        for col in range(N):
            
            # 알고리즘 적용
            move = DFS(rooms, [row, col])

            # 최대값 갱신, 방 번호 덮어쓰기
            if(move > max):
                max = move
                min_room = rooms[row][col]

            # 최대값이 같은 상황에서 방 번호가 더 작은 쪽을 선택
            elif(move == max and min_room > rooms[row][col]):
                min_room = rooms[row][col]

    # 결과 출력
    print(f'#{t} {min_room} {max}')