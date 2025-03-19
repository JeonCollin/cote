'''
최소힙: |연산을 거친 현재 수 - 목표 수| 가 작을수록 좋다
[연산결과, 차이, cnt]
'''
def empty():
    return front == rear

def full():
    return front == (rear+1)%a

def enqueue(item):
    global rear

    # full
    if(full() == True):
        print('full')

    # enqueue
    else:
        rear = (rear+1)%a
        heap[rear] = item
    
        
def dequeue():
    global front

    # empty
    if(empty() == True):
        print('empty')

    # dequeue
    else:
        #현재 front에는 값이 없다
        front = (front+1)%a
        return heap[front]


def BFS():
    global N, M
    
    visited = [0]*1000001
    
    # 현재 수, 차이, cnt 저장
    enqueue([N, M-N, 0])
    visited[N] = 1
    
    while True:
        # print(heap)
        # 현재 수, cnt 받기
        temp = dequeue()
        
        # 4가지 연산 결과를 적용한다
        for i in range(4):
            # +1
            if(i == 0):
                num = temp[0]+1
            # -1
            elif(i == 1):
                num = temp[0]-1
            # *2
            elif(i == 2):
                num = temp[0]*2
            # -10
            else:
                num = temp[0]-10
            
            if(visited[num] != 0):
                continue
            
            # 방문 기록
            visited[num] = 1
            
            # 연산 횟수 증가
            cnt = temp[2] + 1
                
            # 만약 목표한 값이 되면 횟수 리턴
            if(num == M):
                return cnt
            
            # 100만을 넘거나, 0 이하가 되면 필요 없다
            if(num >= 2*M or num <= 1):
                continue
            # 결과 저장
            enqueue([num, abs(M-num), cnt])
     
    
    

T = int(input())

for t in range(1, T+1):
    
    # N: 현재 수, M: 원하는 수
    N, M = list(map(int, input().split()))
    
    a = 1000000
    
    # heap 초기화
    heap = [0]*a
    front = 0
    rear = 0
    
    # 결과 출력
    print(f'#{t} {BFS()}')