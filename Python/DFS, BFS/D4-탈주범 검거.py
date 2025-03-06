# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def empty():
    return front == rear

def full():
    return rear == N*M*L-1

def enqueue(item):
    global rear

    if(full() == True):
        print('full')

    else:
        rear += 1
        queue[rear] = item

def dequeue():
    global front

    if(empty() == True):
        return False

    else:
        front += 1
        return queue[front]

def BFS(myList):
    global R
    global C

    # 방문리스트 생성
    visited = [[0]*M for _ in range(N)]

    # 현재 위치 큐에 저장
    enqueue([R, C])

    # 알고리즘
    while True:
        
        # 위치 받기
        node = dequeue()
        row = node[0]
        col = node[1]

        # 방문 기록
        if(visited[row][col] == 0):
            visited[row][col] = 1

        # 현재 위치에서 연결된 부분 확인
        # 방향벡터 적용
        for i in range(4):
            ROW = row + drow[i]
            COL = col + dcol[i]
            adj = connected(i)


            # 범위를 벗어나지 않고
            # 방문한 적 없고
            # 연결되어있는 곳이라면 갈 수 있다.
            if(0 <= ROW < N and 0 <= COL < M
               and visited[ROW][COL] == 0):
                
                # 현재 파이프와 다음 파이프 확인
                pipe_now = myList[row][col]
                pipe_next = myList[ROW][COL]

                # 연결되어 있는 파이프라면 갈 수 있다.
                if(adj[pipe_now][pipe_next] != 0):
                    # 큐에 저장
                    enqueue([ROW, COL])
                    # 방문 누적
                    visited[ROW][COL] = visited[row][col] + 1

                    # 제한된 시간 L을 넘어가면 끝
                    if(visited[ROW][COL] == L+1):
                        visited[ROW][COL] = 0
                        return visited
        
        # 큐에 원소가 없다면 끝
        if(empty() == True):
            return visited
        
        # # 검증용
        # for i in range(N):
        #     print(visited[i])


def connected(direction):
    # 파이프 연결 상태를 확인하는 함수
    # 현재 위치 >(상)> 다음 위치
    if(direction == 0):
        connect_list = [ [0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 2, 0, 0, 5, 6, 0]
                        ,[0, 1, 2, 0, 0, 5, 6, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 2, 0, 0, 5, 6, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 2, 0, 0, 5, 6, 0]]

    # 현재 위치 >(하)> 다음 위치
    if(direction == 1):
        connect_list = [ [0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 2, 0, 4, 0, 0, 7]
                        ,[0, 1, 2, 0, 4, 0, 0, 7]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 2, 0, 4, 0, 0, 7]
                        ,[0, 1, 2, 0, 4, 0, 0, 7]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]]

    # 현재 위치 >(좌)> 다음 위치
    if(direction == 2):
        connect_list = [ [0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 0, 3, 4, 5, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 0, 3, 4, 5, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 0, 3, 4, 5, 0, 0]
                        ,[0, 1, 0, 3, 4, 5, 0, 0]]
        
    # 현재 위치 >(우)> 다음 위치
    if(direction == 3):
        connect_list = [ [0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 0, 3, 0, 0, 6, 7]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 1, 0, 3, 0, 0, 6, 7]
                        ,[0, 1, 0, 3, 0, 0, 6, 7]
                        ,[0, 1, 0, 3, 0, 0, 6, 7]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ,[0, 0, 0, 0, 0, 0, 0, 0]
                        ]

    return connect_list

T = int(input())

for t in range(1, T+1):

    # N: 행 길이, M: 열 길이, R, C: 맨홀뚜껑, L: 탈출 후 소요된 시간
    N, M, R, C, L = list(map(int, input().split()))

    # N x M 행렬 받기
    mylist = [list(map(int, input().split())) for _ in range(N)]

    # 큐 초기화
    queue = [0]*N*M*L
    front = -1
    rear = -1

    vistedlist = BFS(mylist)

    # 검증용
    # for i in range(N):
    #     print(vistedlist[i])

    # 만들어낸 visited list를 순회하며 범인이 있을 곳을 찾는다
    # 0만 아니라면 다 있을 수 있다.
    cnt = 0

    for i in range(N):
        for j in range(M):
            if(vistedlist[i][j] != 0):
                cnt += 1

    # 결과 출력
    print(f'#{t} {cnt}')