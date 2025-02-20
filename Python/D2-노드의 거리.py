def empty():
    return front == rear

def full():
    return rear == V-1

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
        print('full')

    else:
        front += 1
        return queue[front]
    

def BFS(adj_arr):
    global V
    global start
    global end

    # 방문리스트 생성: 1번부터 시작임
    visited = [0]*(V+1)

    # 시작점 삽입, 방문기록
    enqueue(start)
    visited[start] = 1

    # 큐에 원소가 있는 동안
    while True:

        # 현재 위치 받기
        node = dequeue()

        # 현재 위치에서 갈 수 있는 곳 찾기
        for next in range(len(adj_arr[node])):
            # 인접해있고, 방문한 적이 없다면
            if(adj_arr[node][next] == 1 and visited[next] == 0):
                # 장소 기록
                enqueue(next)
                # 방문기록: 가는데 걸리는 횟수
                visited[next] = visited[node] + 1
                # 만약 끝 점이라면 가는데 걸린 횟수 리턴
                if(next == end):
                    return visited[next] - 1
                
        # 못가는 경우: 큐가 비어있다
        # 근데 양방향이라 그럴 일 없음
        if(empty() == True):
            return 0


T = int(input())

for t in range(1, T+1):

    # V 노드 수, E 간선 수
    V, E = list(map(int, input().split()))

    # 인접행렬 생성: 1번 노드부터 시작
    adj_arr = [[0]*(V+1) for _ in range(V+1)]

    for e in range(E):
        v1, v2 = list(map(int, input().split()))
        # 양방향임
        adj_arr[v1][v2] = 1
        adj_arr[v2][v1] = 1

    # 시작, 끝
    start, end = list(map(int, input().split()))

    # queue init
    queue = [0]*V
    front = -1
    rear = -1

    print(f'#{t} {BFS(adj_arr)}')