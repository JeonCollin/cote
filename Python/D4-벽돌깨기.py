import copy

# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

##### 큐에 사용되는 함수 #####
def empty():
    return front == rear

def full():
    return rear == H*W - 1

def enq(item):
    global rear
        
    if(full() == True):
        print('full')
        
    else:
        rear += 1
        queue[rear] = item
        
def deq():
    global front
    
    if(empty() == True):
        return False
    
    else:
        front += 1
        return queue[front]
    
##############################

def repeat_permutation(idx):
    global block_min
    global brick
    global origin_brick
    global queue
    global front
    global rear
    
    # nPr 순열 완성
    if(idx == N):
        
        # 순열 순서대로 터트린다
        for j in range(N):
            # 열이 선택되었으니까 행을 찾아야 한다
            for k in range(H):
                if(k != 0):
                    row = k
                    break
            # 터트리고
            BFS(row, PI[j])
            # 중력 적용
            gravity()
            
        for c in range(H):
            print(brick[c])
        print()
        
        # N번 던졌으면 남은 블럭 수를 찾는다
        cnt = 0
        
        for a in range(H):
            for b in range(W):
                if(brick[a][b] != 0):
                    cnt += 1
                    
        # 최소값 갱신          
        if(cnt < block_min):
            cnt = block_min
            
        # 벽돌리스트 다시 초기화
        # 큐도 초기화
        brick = copy.deepcopy(origin_brick)
        queue = [0]*W*H
        front = -1
        rear = -1
        
        
    # 순열 리스트 고르기
    else:
        for i in range(W):
            PI[idx] = idx_list[i]
            repeat_permutation(idx+1)
                


def gravity():
    # 중력을 적용하는 함수
    # 0인 부분이 있다면 아래로 당긴다
    global brick
    global W, H
    
    # 아래에서 위로 탐색: 그래야 중력 받고 아래로 내려온다
    for col in range(W):
        # 맨 위는 굳이 안봐도 된다
        for row in range(H-1, 0, -1):
            i = 0
            # 만약 빈 공간이 있다면
            if(brick[row][col] == 0):
                # 저 위에 있는 블럭을 찾는다
                while True:
                    
                    i += 1
                    
                    # 찾았으면 바꾼다(범위를 벗어나지 않는 선에서)
                    if(brick[row-i][col] != 0):
                        brick[row][col], brick[row-i][col] = brick[row-i][col], brick[row][col]
                        break
                    
                    # 없다면 끝낸다
                    if(row - i < 0):
                        break


def BFS(row, col):
    # 구슬을 터트리는 함수
    
    # 방문리스트 생성
    visited = [[0]*W for _ in range(H)]
    
    # 일단 현재 위치, 폭발범위 기록
    enq([row, col, brick[row][col]])
    visited[row][col] = 1
    
    # 알고리즘
    while True:
        
        # 위치 받기
        node = deq()
        n = node[2]
        
        # 다음 위치 폭탄 터트리기
        for i in range(4):
            for j in range(n):
                ROW = node[0] + drow[i]*j
                COL = node[1] + dcol[i]*j
                
                # 범위를 벗어나지 않게 제한
                # 방문한 적 없는 곳이라면 터트린다
                if(0 <= ROW < H and 0 <= COL < W
                   and visited[ROW][COL] == 0):
                    
                    # 만약 폭발범위가 2이상이라면 기록한다
                    if(brick[ROW][COL] >= 2):
                        enq([ROW, COL, brick[ROW][COL]])
                        
                    # 터트린 흔적을 남긴다
                    brick[ROW][COL] = 0
                    visited[ROW][COL] = 1
                  
        # 갈 할수 있는 모든 곳을 했다면 끝  
        if(empty() == True):
            return
                    


            
T = int(input())

for t in range(1, T+1):

    
    # N 번 구슬 던짐, 벽돌: W x H 
    N, W, H = list(map(int, input().split()))
    
    # 최소값 초기화
    block_min = W*H
    
    # 인덱스의 리스트 생성
    idx_list = [hi for hi in range(10)]
    PI = [0]*N    
    
    # 배열 받기
    brick = [list(map(int, input().split())) for _ in range(H)]
    origin_brick = copy.deepcopy(brick)
    
    # 큐 초기화
    queue = [0]*W*H
    front = -1
    rear = -1
    
    # 구슬을 쏠 중복리스트를 생성함
    repeat_permutation(0)
    
    
    # 결과 출력
    print(f'#{t} {block_min}')