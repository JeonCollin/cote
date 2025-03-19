# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [ 0, 0,-1, 1]

# 최소힙
def enqueue(item):
    global rear
    global root
    
    # rear에 원소 넣는다
    rear += 1
    heap[rear] = item
    
    # parent / child 크기 비교
    # 아래에서 위로
    c = rear
    p = c//2
    
    # root까지 비교
    while(p >= root):
        
        # 자식이 부모보다 작다면 스왑
        if(heap[p][2] > heap[c][2]):
            heap[p], heap[c] = heap[c], heap[p]
        
        # 한 칸 위로 올라간다
        c = p
        p = c//2
        
def dequeue():
    global rear
    global root
    
    # root에서 원소를 뺀다
    temp = heap[root]
    # root에 rear원소를 넣고 삭제
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1
    
    # 루트와 자식 크기 비교
    p = root
    c = 2*p
    
    # c가 rear에 갈 때 까지
    while(c <= rear):
        # 만약 오른쪽 자식이 존재하고
        # 왼쪽보다 작다면 걔가 기준
        if(c+1 <= rear and heap[c+1][2] < heap[c][2]):
            c = c+1
            
        # 자식과 부모 비교
        # 자식이 더 작다면 바꾼다
        if(heap[c][2] < heap[p][2]):
            heap[p], heap[c] = heap[c], heap[p] 
            # 아래로 내려간다
            p = c
            c = 2*p
        
        # 아니면 끝낸다
        else:
            break
        
    # 크기 비교가 끝났으면 루트 리턴
    return temp


def BFS(start, end):
    global roads
    global rear
    
    # 방문리스트 생성
    visited = [[0]*N for _ in range(N)]
    
    # 현재 위치 기록
    # row, col, 걸린 시간
    enqueue([start, end, 0])
    visited[0][0] = 1
    
    # BFS
    while True:
        # print(heap)
        # for j in range(N):
        #     print(visited[j])
        # print()
        # 위치 받기
        node = dequeue()
        # 갈 수 있는 인접 지역 확인
        for i in range(4):
            ROW = node[0] + drow[i]
            COL = node[1] + dcol[i]
            
            # 방문한 적 없고, 영역을 벗어나지 않으면 go
            if(0 <= ROW < N and 0 <= COL < N and
               visited[ROW][COL] == 0):
                visited[ROW][COL] = 1
                # 걸린 시간 카운팅
                time = node[2] + roads[ROW][COL]
                # 만약 끝 지점이면 최소 시간 리턴
                if(ROW == N-1 and COL == N-1):
                    return time
                # 그 위치 기록
                enqueue([ROW, COL, time])
                
                
        # 만약 heap이 비었다면 0 리턴
        # 무조건 갈 수 있기 때문에 필요없을듯
        # if(rear == 0):
        #     return 0
    

    
T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    roads = [list(map(int, input())) for _ in range(N)]
    
    # heap 초기화
    heap = [0]*N**2
    root = 1
    rear = 0
    
    # 최소 시간
    min_time = BFS(0,0)
    
    # 결과 출력
    print(f'#{t} {min_time}')