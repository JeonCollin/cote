'''
최대힙: 도착 인덱스가 큰 것이 우선
1. 출발지에서 충전을 해서
2. 갈 수 있는 인덱스를 모두 enqueue
3. 갈 수 있는 최대 인덱스가 큰 것이 우선순위

      출       도
       0 1 2 3 4
충전지 2 3 1 1 ()
        eqeq
최대     4 3

'''

def enqueue(item):
    global rear
    global root
    
    # 일단 집어 넣는다
    rear += 1
    heap[rear] = item
    
    # 자식 / 부모 크기 비교
    # 아래에서 위로
    c = rear
    p = c // 2
    
    # 루트랑 비교할 때 까지
    while(p >= root):
        
        # 자식이 더 크다면 위로 보냄
        if(heap[c][1] >= heap[p][1]):
            heap[c], heap[p] = heap[p], heap[c]
            
        # 위로 한 칸 올라간다
        c = p
        p = c // 2
        
        
def dequeue():
    global rear
    global root
    
    # 일단 빼낸다
    temp = heap[root]
    # 가장 마지막 원소를 루트에 넣는다
    heap[root] = heap[rear]
    # 한 칸 당긴다
    heap[rear] = 0
    rear -= 1
    
    # 부모 / 자식 크기 비교
    # 위에서 아래로
    p = root
    c = 2*p
    
    # 로테이션
    # 자식이 rear가 될 때 까지
    while(c <= rear):

        # 만약 오른쪽 자식이 존재하고
        # 왼쪽보다 크면 비교 대상이 오른쪽
        if(c+1 <= rear and heap[c][1] <= heap[c+1][1]):
            c += 1
            
        # 자식이 부모보다 크면 올린다
        if(heap[c][1] >= heap[p][1]):
            heap[p], heap[c] = heap[c], heap[p]
            # 아래로 내려간다
            p = c
            c = 2*p
        
        # 부모가 크면 그냥 끝
        else:
            break
       
        
            
    # 로테이션이 끝났으면 값 리턴
    return temp
    

def BFS(stop_list):
    global N
    
    # 시작점 기록
    # 현재 인덱스, 도착인덱스, 충전 횟수
    enqueue([0, 0 + stop_list[0], 0])
    
    while True:
        #print(heap)
        # 위치, 도착, 충전횟수 받기
        temp = dequeue()
        stop = temp[0]
        distance = temp[1]
        cnt = temp[2]
        
        # 갈 수 있는 곳 모두 enq
        # 현재 정류장 제외
        for i in range(stop+1, distance + 1):
            
            # 현재 인덱스
            now = i
            # 도착 인덱스
            arrive = i + stop_list[i]
            # 충전횟수
            charge = cnt + 1
            # 만약 도착지면 끝남
            if(arrive >= N-1):
                return charge     
            
            # 충전횟수 계산
            enqueue([now, arrive, charge])
            
        # 큐가 비었다면 도착 못하는거임
        if(rear == 0):
            return 0



T = int(input())

for t in range(1, T+1):
    
    # 정류장 수 N, 버스정류장 N개
    mylist = list(map(int, input().split()))
    N = mylist[0]
    stop_list = mylist[1:]
    stop_list = stop_list + [0]
    
    # 출발지[0]에서 무조건 충전함
    # 정류장: 0 1 2 3 4
    # 충전지: 2 3 1 1 ()
    #        출       도
    
    # 힙 초기화
    heap = [0]*N
    root = 1
    rear = 0
    
    # 결과 출력
    print(f'#{t} {BFS(stop_list)}')