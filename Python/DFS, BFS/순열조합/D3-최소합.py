### 힙 위한 함수 ###
def enqueue(item):
    # 최소 힙
    global rear
    global root
    
    # 일단 맨 뒤에 아이템을 넣는다
    rear += 1
    heap[rear] = item
    
    # 부모, 자식간에 크기 비교
    c = rear
    p = c//2
    
    # 아래에서 위로 올라가면서 부모/자식 비교
    # 언제까지? 루트까지!
    while(p >= root):
        
        # 자식이 부모보다 작다면
        if(heap[c][2] < heap[p][2]):
            # 바꾼다
            heap[c], heap[p] = heap[p], heap[c]
            
        # 한 칸 위로 올라간다
        c = p
        p = c//2
        
def dequeue():
    # 최소 힙
    global rear
    global root
    
    # 일단 루트에서 빼내고 
    # 마지막 원소를 채워넣는다
    temp = heap[root]
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1
    
    # 부모, 자식간에 크기 비교
    p = root
    cl = 2*p
    cr = 2*p + 1
    
    # 위에서 아래로 내려가면서 부모/자식 비교
    # 언제까지? 자식이 rear가 될 때 까지!
    while(cl <= rear or cr <= rear):
        # 오른쪽 자식이 존재하고
        # 부모보다 작다면
        if(heap[cr] != 0 and heap[cl] > heap[cr] and heap[cr][2] < heap[p][2]):
            # 오른쪽 자식이 왼쪽 자식보다 작고 부모보다 작다면
            if(heap[cl] > heap[cr] and heap[cr][2] < heap[p][2]):
                # 바꾼다
                heap[cr], heap[p] = heap[p], heap[cr]
                p = cr
                
            # 왼쪽 자식이 더 작고 부모보다 작다면
            if(heap[cl] < heap[cr] and heap[cl][2] < heap[p][2]):
                # 바꾼다
                heap[cl], heap[p] = heap[p], heap[cl]
                p = cl
            
        # 왼쪽 자식 비교
        if(heap[cr] == 0 and heap[cl] != 0 and heap[cl][2] < heap[p][2]):
            heap[cl], heap[p] = heap[p], heap[cl]
            p = cl
            
        # 둘 다 해당 없다면 그냥 하나 선택
        else:
            p = cl
            
        # 한 칸 내려간다
        cl = 2*p
        cr = 2*p + 1
    
    # 결과 리턴
    return temp
            
#####################
# 상하좌우
drow = [-1, 1, 0 ,0]
dcol = [0, 0, -1, 1]

def BFS(row, col):
    # 최단거리 구하기
    # 방문리스트 생성
    visitied = [[0]*N for _ in range(N)]
    
    # 시작점 저장
    # row, col, 합계
    enqueue([row, col, mylist[row][col]])
    visitied[row][col] = 1
    
    # 알고리즘
    while True:
        # for i in range(N):
        #     print(visitied[i])
        # print()
        #print(heap)
        # 시작점 받기
        node = dequeue()
        row = node[0]
        col = node[1]
        num = node[2]

        # 인접 지역 방문
        for i in range(4):
            ROW = row + drow[i]
            COL = col + dcol[i]
            
            # 범위를 벗어나지 않고
            # 방문한 적이 없다면
            if(0 <= ROW < N and 0 <= COL < N
               and visitied[ROW][COL] == 0):
                # 합계 기록
                sumn = num + mylist[ROW][COL]
                
                # 만약 끝지점이면 끝내자
                if(ROW == N-1 and COL == N-1):
                    return sumn
                # 방문한다
                enqueue([ROW, COL, sumn])
                visitied[ROW][COL] = 1
                


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    mylist = [list(map(int, input().split())) for _ in range(N)]
    
    # 최소힙 초기화
    heap = [0]*N*N
    root = 1
    rear = 0
    
    # 결과출력
    print(f'#{t} {BFS(0,0)}')