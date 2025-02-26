# 상 하 좌 우
drow = [-1, 1,  0, 0]
dcol = [ 0, 0, -1, 1]

def sort():
    global front
    global rear
    global queue
    global accumulate

    # bubble sort
    # 오름차순
    for i in range(rear, 0, -1):
        for j in range(front, i):
            # 누적된 장애물 에서
            # 큐에 있는 원소가 인덱스가 되는
            # 앞에 있는 수가 더 크다면
            if(accumulate[queue[j][0]][queue[j][1]] > accumulate[queue[j+1][0]][queue[j+1][1]]):
                # swap
                queue[j], queue[j+1] = queue[j+1], queue[j]

def empty():
    return front == rear

def full():
    return rear == N**2 - 1

# 우선순위 큐
def enqueue(item):
    global rear

    if(full() == True):
        print(full)

    # enqueue할 때 값을 비교해서
    # 우선순위가 높은 것 먼저 
    # 앞으로 넣으면 되지 않을까?
    else:
        # 일단 넣는다
        rear += 1
        queue[rear] = item
        # 정렬 한다
        sort()
        

def dequeue():
    global front

    if(empty() == True):
        return False
    
    else:
        # 0으로 초기화 한다
        queue[front] = 0
        front += 1
        return queue[front]
    
def BFS(roads):
    global N

    # 방문리스트 생성
    visited = [[0]*N for _ in range(N)]

    # 현재 위치를 큐에 넣는다
    start = [0, 0]
    enqueue(start)

    # 방문 기록
    visited[start[0]][start[1]] = 1

    # 알고리즘
    while True:

        # 위치를 큐에서 받는다
        node = dequeue()

        # 주변에 갈 수 있는 곳을 담는다
        for i in range(4):

            row = node[0] + drow[i]
            col = node[1] + dcol[i]

            # 범위를 벗어나지 않았다면 갈 수 있다.
            # 방문하지 않았다면 간다
            if(0 <= row < N and 0 <= col < N
               and visited[row][col] == 0):
                # 방문 기록, 장애물 수를 누적한다
                visited[row][col] = 1
                accumulate[row][col] += accumulate[node[0]][node[1]]
                # 갈 수 있는 곳을 큐에 기록한다
                enqueue([row, col])
                # 만약 끝지점이면 끝난거다.
                if([row, col] == [N-1, N-1]):
                    return
        


T = int(input())

for t in range(1, T+1):

    N = int(input())

    # 큐 초기화
    queue = [0]*(N**2)
    front = -1
    rear = -1

    # 도로 정보 받기
    roads = [list(map(int, input())) for _ in range(N)]
    
    # 장애물 누적 리스트 생성
    accumulate = [[roads[i][j] for j in range(N)] for i in range(N)]

    BFS(roads)

    # 결과출력
    print(f'#{t} {accumulate[N-1][N-1]}')
    # for i in range(N):
    #     print(accumulate[i])