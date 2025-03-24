'''
대표 노드를 제외한 노드에서 dikjstra로 방문
출발 >> dikjstar(최단경로) >> 도착(인수의 집) : 인수의 집에 도착하면 방문리스트 초기화, 시작 <-> 도착점 바뀜
출발(인수의 집) >> 최단경로 >> 도착(원래 포인트): 최단 복귀경로 리턴

도착하면 최단경로의 최대값 갱신
'''
import heapq

def enqueue(item):
    global rear
    global root

    # rear에 원소 넣기
    rear += 1
    heap[rear] = item

    # 부모와 비교
    # 위에서 아래로
    c = rear
    p = c//2

    while(p >= root):
        # 부모가 자식보다 크다면 바꾼다
        if(heap[p] >= heap[c]):
            heap[p], heap[c] = heap[c], heap[p]

        # 위로 올라가서 비교
        c = p
        p = c//2

def dequeue():
    global rear
    global front

    # root에서 원소 빼기
    temp = heap[root]
    # rear에서 root에 원소 넣기
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1

    # 자식과 비교
    # 위에서 아래로
    p = root
    c = 2*p

    while(c <= rear):
        # 오른쪽 자식이 존재하고, 좌보다 작다면 우선
        if(c+1 <= rear and heap[c+1] <= heap[c]):
            c += 1

        # 부모가 자식보다 크면 바꾼다
        if(heap[p] >= heap[c]):
            heap[p], heap[c] = heap[c], heap[p]
            # 내려간다
            p = c
            c = 2*p

        # 아니면 멈춘다
        else:
            break

    # 결과 반환
    return temp

def Dikjstra(start, end):
    global adj_list

    # 방문리스트 생성
    visited = [0]*(N+1)

    # 시작 위치 받기
    # [가중치, 위치]
    heapq.heappush(heap, [0, start, 0])
    # 시작점을 초기화한다
    visited[start] = -1

    while True:

        # 위치 받기
        temp = heapq.heappop(heap)
        node = temp[1]

        # 거리 갱신
        temp[2] += temp[0]

        # 시작점으로 돌아왔으면 최단경로 리턴
        if(temp[0] != 0 and node == start):
            return temp[2]

        # 방문기록
        visited[node] += 1


        # 현재 위치에서 갈 수 있는 곳 받기
        for i in range(1, N+1):
            # 방문한 적 없고
            # 연결되어있다면 go
            if(visited[node] == 0 and adj_list[node][i] != 0):
                # 위치 저장: [가중치, 다음 위치]
                heapq.heappush(heap, [adj_list[node][i], i, temp[2]])


T = int(input())

for t in range(1, T+1):

    # 1~N 개의 집, M 개의 줄에 걸쳐 정보를 줌, X 인수의 집
    N, M, X = list(map(int, input().split()))

    # 인접행렬 생성
    adj_list = [[0]*(N+1) for _ in range(N+1)]

    for m in range(M):
        # x에서 y로 이동하는데 c의 시간
        x, y, c = list(map(int, input().split()))

        # 단방향임
        adj_list[x][y] = c

    # 힙 초기화(개념적으로만 구현)
    heap = [0]*N
    root = 1
    rear = 0

    # 최대값
    maxx = 0
    
    # 모든 노드에서 시작하며 최대값 갱신
    for i in range(1, N+1):
        # 인수 본인 집은 제외
        if(i == X):
            continue
        
        time = Dikjstra(i, X)

        # 최대값 갱신
        if(time > maxx):
            maxx = time


    # 결과 출력
    print(f'#{t} {time}')