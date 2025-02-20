def isEmpty():
    return rear == front

def isFull():
    return rear == N**2 - 1

def enqueue(item):
    global rear

    if(isFull() == True):
        print('isFull')

    else:
        rear += 1
        queue[rear] = item

def dequeue():
    global front

    if(isEmpty() == True):
        print('isEmpty')

    else:
        front += 1
        return queue[front]
    

def BFS(maze):
    global start
    global N

    # 상 하 좌 우
    drow = [-1, 1,  0, 0]
    dcol = [ 0, 0, -1, 1]

    # 1단계: 방문리스트 생성
    visited = [[0]*N for _ in range(N)]

    # 2단계: 시작점 enqueue, 방문 기록
    enqueue(start)
    visited[start[0]][start[1]] = 1

    # 3단계: 큐가 비어있지 않는 동안 반복
    while True:

        # 4단계: 현재 위치 받기
        node = dequeue()

        # 5단계: 갈 수 있는 위치 확인
        for i in range(4):
            ROW = node[0] + drow[i]
            COL = node[1] + dcol[i]

            # 미로를 벗어나지 않으면
            # 벽이 아니라면
            # 방문한 적이 없다면
            if(0 <= ROW < N and 0 <= COL < N 
               and maze[ROW][COL] != 1
               and visited[ROW][COL] == 0):
                # 연결된 위치들을 큐에 넣는다
                enqueue([ROW, COL])
                # 방문기록: 누적으로 몇 번 걸렸는지
                visited[ROW][COL] = visited[node[0]][node[1]] + 1
                # 종료조건: 끝 점일 때 걸린 횟수 출력
                # 시작, 끝 카운트는 빼야 함
                if(maze[ROW][COL] == 3):
                    return visited[ROW][COL] - 2
                
        # 종료조건: 큐가 비어있을 때
        # 그니까 끝까지 못가는 경우임
        if(isEmpty() == True):
            return 0
                

T = int(input())

for t in range(1, T+1):

    # 미로크기
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 출발, 도착점 찾기
    for i in range(N):
        for j in range(N):

            if(maze[i][j] == 2):
                start = [i, j]

            if(maze[i][j] == 3):
                end = [i, j]

    # 큐 초기화
    queue = [0]*(N**2)
    front = -1
    rear = -1

    # 결과 출력
    print(f'#{t} {BFS(maze)}')