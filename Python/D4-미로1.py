# def isEmpty():
#     return front == rear

# def isFull():
#     return rear == 255

# def enqueue(item):
#     global rear

#     # full
#     if(isFull() == True):
#         print('full')

#     # enqueue
#     else:
#         rear += 1
#         queue[rear] = item

# def dequeue():
#     global front

#     # empty
#     if(isEmpty() == True):
#         print('empty')

#     # dequeue
#     else:
#         front += 1
#         return queue[front]
    
# def BFS(maze):
#     global start

#     # 상 하 좌 우
#     drow = [-1, 1,  0, 0]
#     dcol = [ 0, 0, -1, 1]

#     # 2차원 방문 리스트 생성
#     visited = [[0]*16 for _ in range(16)]

#     # 시작점 삽입
#     enqueue(start)

#     # 방문 기록
#     visited[start[0]][start[1]] = 1

#     # 큐에 원소가 있는 동안
#     while True:

#         # 현재 이동할 노드 지정, 방문 기록
#         node = dequeue()

#         # print(node)
#         # for k in range(16):
#         #     print(visited[k])

#         # 갈 수 있는 노드 확인
#         for i in range(4):
#             ROW = node[0] + drow[i]
#             COL = node[1] + dcol[i]
#             # 미로를 벗어나지 않도록
#             # 벽이 아닌 곳이라면
#             # 방문한 적이 없다면
#             if (0 <= ROW < 16 and 0 <= COL < 16
#                 and maze[ROW][COL] != 1
#                 and visited[ROW][COL] == 0):
#                 # 모두 queue에 넣는다
#                 enqueue([ROW, COL])
#                 # 방문 기록(얼마나 걸렸는지)
#                 visited[ROW][COL] = visited[node[0]][node[1]] + 1
#                 # 끝 지점이라면 리턴
#                 if(maze[ROW][COL] == 3):
#                     return 1
                
#         # 끝에 도달하지 못하면 리턴
#         if(isEmpty() == True):
#             return 0



# for t in range(1, 11):
#     T = int(input())

#     # 16 x 16 미로 받기
#     maze = [list(map(int, input())) for _ in range(16)]

#     # 큐 초기화
#     queue = [0] * 256
#     front = -1
#     rear = -1

#     # 시작점, 도착점 찾기
#     for i in range(16):
#         for j in range(16):
            
#             # 시작점
#             if(maze[i][j] == 2):
#                 start = [i, j]
                
#             # 도착점
#             if(maze[i][j] == 3):
#                 end = [i, j]

#     # 결과 출력
#     print(f'#{t} {BFS(maze)}')


def push(item):
    global top

    # 일단 top 증가
    top += 1

    # overflow
    if(top == len(stack)):
        print('overflow')

    else:
        stack[top] = item


def pop():
    global top

    # overflow
    if(top == -1):
        return False
    
    else:
        top -= 1
        return stack[top+1]
    
def DFS_iterate(maze):
    global N
    global start

    # 방문리스트 생성
    visited = [[0]*N for _ in range(N)]
    node = start

    while True:
        # print(node)
        # 방문기록
        if(visited[node[0]][node[1]] == 0):
            visited[node[0]][node[1]] = 1

        # 현재 위치에서 방문할 수 있는 곳 확인
        for i in range(4):
            ROW = node[0] + drow[i]
            COL = node[1] + dcol[i]

            # 영역을 벗어나지 않고
            # 벽이 아니고
            # 방문하지 않았다면
            if(0 <= ROW < N and 0 <= COL < N
               and maze[ROW][COL] != 1
               and visited[ROW][COL] == 0):
                # 현재 위치 저장
                push(node)
                # 방문 누적
                visited[ROW][COL] = visited[node[0]][node[1]] + 1
                # 노드 이동
                node = [ROW, COL]
                
                # 종료조건: 끝 지점
                if(maze[ROW][COL] == 3):
                    return 1
                
                break
                
        # 길이 없는 경우 되돌아간다   
        else:
            node = pop()
            # 근데 underflow면 종료
            if(node == False):
                return 0

def DFS_recursion(start):
    global used
    global maze
    global ans

    # 첫 장소 방문 기록
    used[start[0]][start[1]] = 1

    # 현재 위치에서 갈 수 있는 곳 확인
    for i in range(4):
        ROW = start[0] + drow[i]
        COL = start[1] + dcol[i]

        # 영역을 벗어나지 않고
        # 벽이 아니고
        # 방문한 적 없다면
        if(0 <= ROW < N and 0 <= COL < N
               and maze[ROW][COL] != 1
               and used[ROW][COL] == 0):
            # 방문 기록
            used[ROW][COL] = 1
            node = [ROW, COL]

            # 끝 지점이라면 종료
            if(maze[ROW][COL] == 3):
                ans = 1

            # 해당 노드로 이동
            DFS_recursion(node)


# 상 하 좌 우
drow = [-1, 1,  0, 0]
dcol = [ 0, 0, -1, 1]

for t in range(1, 11):

    T = int(input())
    N = 16

    # 미로 받기
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if(maze[i][j] == 2):
                start = [i, j]

    # stack 초기화
    stack = [0]*(N**2)
    top = -1
    
    # 재귀형
    # used 생성
    ans = 0
    used = [[0]*N for _ in range(N)]
    DFS_recursion(start)

    # for i in range(N):
    #     print(used[i])

    print(f'#{t} {ans}')

    # 반복형
    # visite = DFS_iterate(maze)

    # for i in range(N):
    #     print(visite[i])
    # 결과 출력
    # print(f'#{t} {DFS_iterate(maze)}')