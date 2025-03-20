def enqueue(item):
    global root
    global rear
    
    # rear에 item 저장
    rear += 1
    heap[rear] = item
    
    # 부모와 크기비교
    # 아래에서 위로
    c = rear
    p = c//2
    
    # 부모가 루트 될 때 까지 비교
    while(p >= root):
        # 최소힙
        # 자식이 더 작다면 바꾼다
        if(heap[c][1] <= heap[p][1]):
            heap[c], heap[p] = heap[p], heap[c]
        
        # 위로 올라간다
        c = p
        p = c//2
        
    
def dequeue():
    global root
    global rear
    
    # root에서 출력
    temp = heap[root]
    # rear에서 가져온다
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1
    
    # 루트에서 내려가면서 크기 비교
    p = root
    c = 2*p
    
    # 자식이 rear가 될 때 까지
    while(c <= rear):
        # 오른쪽 자식이 존재하고
        # 왼쪽보다 작다면 우선
        if(c+1 <= rear and heap[c][1] >= heap[c+1][1]):
            c = c+1
            
        # 자식과 부모 비교
        # 자식이 더 작다면 바꾼다
        if(heap[p][1] >= heap[c][1]):
            heap[p], heap[c] = heap[c], heap[p]
            # 아래로 내려간다
            p = c
            c = 2*p
            
        # 그게 아니면 그냥 끝
        else:
            break
        
    # 결과 리턴
    return temp


def BFS():
    global adj_arr
    global N
    
    # 현재 노드 기록
    # [현재노드, 거리]
    enqueue([0, 0])
    
    
    # 목적지에 도달할 때 까지
    while True:
        # 현재 위치 받기
        node = dequeue()
        
        # 도착지라면, 거리 출력
        if(node[0] == N):
            return node[1]
        
        # 인접지역 탐색
        for n in range(N+1):
            
            # 연결되어있고
            # 방문한적 없다면 go
            if(adj_arr[node[0]][n] != 0):
                    
                # 이동 거리 계산하기
                distance = node[1] + adj_arr[node[0]][n]
                
                # 해당 위치 enqueue
                enqueue([n, distance])

T = int(input())

for t in range(1, T+1):
    
    # N: 총 노드 수, E: 간선 수
    N, E = list(map(int, input().split()))
    
    # 힙 초기화
    heap = [0]*N*N
    root = 1
    rear = 0
    
    # 인접행렬 생성
    adj_arr = [[0]*(N+1) for _ in range(N+1)]
    
    for e in range(E):
        # 시작, 끝, 거리
        s, e, w = list(map(int, input().split()))
        
        adj_arr[s][e] = w
        
    # 결과 출력
    print(f'#{t} {BFS()}')