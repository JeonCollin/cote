import heapq

def enqueue(item):
    global root
    global rear
    
    # 맨 뒤에 아이템 삽입
    rear += 1
    heap[rear] = item
    
    # 아래에서 위로 올라가며 크기 비교
    c = rear
    p = c//2
    
    # 루트에 도달할 때 가지
    while(p >= root):
        # 자식이 더 작다면 바꾼다
        if(heap[c] <= heap[p]):
            heap[c], heap[p] = heap[p], heap[c]
            
        # 위로 올라간다
        c = p
        p = c//2

def dequeue():
    global rear
    global root
    
    # 루트에서 빼낸다
    temp = heap[root]
    # 맨 뒤에서 루트를 채운다
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1
    
    # 위에서 아래로 비교
    p = root
    c = 2*p
    
    while(c <= rear):
        # 오른쪽이 있다면 먼저 비교
        if(c+1 <= rear and heap[c+1] < heap[c]):
            c += 1
            
        # 부모 자식 크기 비교
        if(heap[p] >= heap[c]):
            heap[c], heap[p] = heap[p], heap[c]
        
        # 아래로 내려간다
        p = c
        c = p*2
        
    # 결과 리턴
    return temp

def Prim(start):
    global x_list
    global y_list
    
    # 방문 리스트 기록
    # 0번 ~ N-1번 섬
    visited = [0]*N
    
    # 현재 위치 기록
    # [이동 거리, 현재위치]
    heapq.heappush(heap, [0, start])
    summ = 0

    
    # Prim
    while True:
        
        # 현재 위치 받기
        dist, node = heapq.heappop(heap)
        # 이미 방문한 노드면 넘긴다
        if(visited[node] == 1):
            continue
        # 아니면 방문기록
        visited[node] = 1      
        # print(dist)
        # 거리, 이동 횟수 계산
        summ += dist

        
        # 0번 >> N-1번: 총 N번 움직임
        # 시작점에서 움직인 것도 포함됨
        if(visited == [1]*N):
            return summ*E
        
        
        # 갈 수 있는 모든 지역 enqueue
        for i in range(N):
            # 방문한 적 없다면 enqueue
            if(visited[i] == 0):
                # 거리 계산
                distance = (x_list[i] - x_list[node])**2 + (y_list[i] - y_list[node])**2
                # 방문 기록
                heapq.heappush(heap, [distance, i])
                

T= int(input())

for t in range(1, T+1):
    
    # 섬의 개수
    N = int(input())
    
    # 섬들의 x좌표
    x_list = list(map(int, input().split()))
    
    # 섬들의 y좌표
    y_list = list(map(int, input().split()))
    
    # 환경 부담 세율
    E = float(input())
    
    # 최소힙 초기화
    heap = []
    root = 1
    rear = 0
    
    minn_cost = Prim(0)
    
    # 결과 출력
    print(f'#{t} {round(minn_cost)}')