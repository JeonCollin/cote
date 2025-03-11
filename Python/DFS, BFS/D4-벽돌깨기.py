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
        pass
        
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

def gravity():
    global brick
    # 중력 적용하는 함수
    # 아래에서 위로 탐색
    for col in range(W):
        for row in range(H-1, 0, -1):
            i = 1
            # 만약 빈 공간이 있다면
            if(brick[row][col] == 0):
                # 위에 있는 벽돌 탐색
                # 인덱스를 벗어나지 않을 때 까지
                while(row - i >= 0):

                    # 만약 벽돌을 찾았다면 바꾼다
                    if(brick[row-i][col] != 0):
                        brick[row-i][col], brick[row][col] = brick[row][col], brick[row-i][col]
                        break

                    i += 1

def repeat_permutation(idx):
    # 중복순열 생성하는 함수
    # 인덱스의 중복순열

    # 최종 길이 = 구슬을 던진 횟수
    if(idx == N):
        # 순열 완성 >> 순열 리스트에 추가
        PIlist.append(PI[:])
        # print(PIlist)
        return

    # 순열을 찾는 단계
    else:
        # 0 ~ W에서 중복순열
        for i in range(W):
            PI[idx] = idx_list[i]
            repeat_permutation(idx+1)


def explosion(row, col):
    global brick
    # 구슬을 던지면 터지는 함수

    # 방문리스트 생성
    visited = [[0]*W for _ in range(H)]

    # 현재 위치 기록
    enq([row, col, brick[row][col]])
    visited[row][col] = 1
    brick[row][col] = 0

    # BFS 적용: 큐가 빌 때 까지
    while True:

        # 종료조건: 큐가 비었다
        if(empty() == True):
            return

        # 현재위치 갱신
        node = deq()
        num = node[2]

        # 방향벡터로 상하좌우 살핀다
        for i in range(4):
            # 터지는 범위도 고려한다
            for j in range(num):
                ROW = node[0] + drow[i]*j
                COL = node[1] + dcol[i]*j

                # 인덱스가 벗어나지 않도록 주의한다
                # 이미 폭탄으로 지워졌으면 굳이 갈 필요 없다
                if(0 <= ROW < H and 0 <= COL < W
                    and visited[ROW][COL] == 0):

                    # 현재 위치의 폭탄이 광범위면 기록
                    if(brick[ROW][COL] >= 2):
                        enq([ROW, COL, brick[ROW][COL]])
                    
                    # 터진 흔적 기록
                    brick[ROW][COL] = 0
                    visited[ROW][COL] = 1

        


T = int(input())

for t in range(1, T+1):

    # N 번 구슬 던짐, 벽돌: W x H 
    N, W, H = list(map(int, input().split()))
    
    # 최소값 초기화
    block_min = W*H
    
    # 인덱스의 리스트 생성
    idx_list = [hi for hi in range(W)]
    PI = [0]*N
    PIlist = []
    # 구슬을 던질 중복순열 생성
    repeat_permutation(0)
    # print(PIlist)
    
    # 배열 받기
    brick = [list(map(int, input().split())) for _ in range(H)]
    origin_brick = copy.deepcopy(brick)

    # 큐 초기화
    queue = [0]*W*H
    front = -1
    rear = -1

    #### 알고리즘 적용 ####

    # 생성된 중복순열의 수 만큼 반복
    for repeat in range(len(PIlist)):

        cnt = 0
        # 구슬을 던지는 횟수 N
        for n in range(N):
            # 인덱스에 맞춰서 구슬을 터트리자
            # 열은 선정 되었으니까 가장 맨 위의 행을 찾아야 한다
            for up in range(H):
                if(brick[up][PIlist[repeat][n]] != 0):
                    break
            
            # 가장 맨 위의 행을 정했다면 구슬을 터트리자
            explosion(up, PIlist[repeat][n])

            # 터트렸으면, 중력을 적용해서 아래로 정렬하자
            gravity()
        
        # 해당 순열에 대한 연산이 끝났으면 0의 개수를 찾자
        for a in range(H):
            for b in range(W):
                if(brick[a][b] != 0):
                    cnt += 1
        
        # 남아있는 최소 벽돌 갱신
        if(cnt < block_min):
            block_min = cnt

        # 근데 남아있는 벽돌 개수가 0이라면 무조건 최소임
        if(block_min == 0):
            break

        ### 검증용 ###
        # for h in range(H):
        #     print(brick[h])
        # print()

        # 다음 루프를 위해 큐와 벽돌 원상복구
        brick = copy.deepcopy(origin_brick)

        queue = [0]*W*H
        front = -1
        rear = -1

    # 결과 출력
    print(f'#{t} {block_min}')