'''
최소힙: 기본 움직임 + 높이 차이
[row, col, fuel]
'''
# (상) 하 (좌) 우
drow = [1, 0]
dcol = [0, 1]

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
        if(heap[c][2] <= heap[p][2]):
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
        if(c+1 <= rear and heap[c][2] >= heap[c+1][2]):
            c = c+1
            
        # 자식과 부모 비교
        # 자식이 더 작다면 바꾼다
        if(heap[p][2] >= heap[c][2]):
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
    global mylist
    global N
    
    # 방문기록
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    
    # 현재 노드 기록
    # [(좌표), 사용 연료]
    enqueue([0, 0, 0])
    
    
    # 목적지에 도달할 때 까지
    while True:
        print(heap)
        # 현재 위치 받기, 방문기록
        node = dequeue()
        
        # for i in range(N):
        #     print(visited[i])
        # print()
        # 인접지역 탐색
        for i in range(2):
            ROW = node[0] + drow[i]
            COL = node[1] + dcol[i]
            
            # 범위를 벗어나지 않고
            # 방문한적 없다면 go
            if(0 <= ROW < N and 0 <= COL < N
               and visited[ROW][COL] == 0):
                
                visited[node[0]][node[1]] = 1
                
                # 높이 차이
                height_difference = mylist[ROW][COL] - mylist[node[0]][node[1]]
                
                # 높이 차이가 양수인것만 신경쓴다
                if(height_difference < 0):
                    height_difference = 0
                    
                # 사용 연료 계산하기
                fuel = node[2] + 1 + height_difference
                
                # 도착지라면, 사용 연료 출력
                if(ROW*COL == (N-1)*(N-1)):
                    return fuel
                
                # 해당 위치 enqueue
                enqueue([ROW, COL, fuel])
    

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    mylist = [list(map(int, input().split())) for _ in range(N)]
    
    # 힙 초기화
    heap = [0]*N*N
    root = 1
    rear = 0
    
    # 결과 출력
    print(f'#{t} {BFS()}')