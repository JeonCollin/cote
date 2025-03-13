def isEmpty():
    return rear == front

def isFull():
    # rear의 다음 위치가 front의 현재 위치이면 포화
    return front == (rear+1)%L

def enqueue(item):
    global rear

    # full
    if(isFull() == True):
        print('full')

    # enqueue
    else:
        rear = (rear+1)%L
        queue[rear] = item

def dequeue():
    global front

    # empty
    if(isEmpty() == True):
        print('empty')

    # dequeue
    else:
        #현재 front에는 값이 없다
        front = (front+1)%L
        return queue[front]

def move_num(numlist, N):

    # 일단 큐에 넣자
    for i in range(N):
        enqueue(numlist[i])

    # 그러고 나서 dequeue 하고
    # 맨 뒤에 붙이고
    # 맨 앞에 있는 글자를 알아낸다
    # M+1번째가 그 수
    for j in range(M+1):
        num = dequeue()
        enqueue(num)

    return num

        

T = int(input())

for t in range(1, T+1):

    #N: 자연수 개수, M 번 숫자 이동
    N, M = list(map(int, input().split()))

    # 자연수 리스트
    # 큐에서 구역을 나눌 때 사용할 거임
    numlist = list( input().split())

    L = M + 1

    # 원형 큐 초기화
    queue = [0]*L
    front = 0
    rear = 0

    # 결과출력
    print(f'#{t} {move_num(numlist, N)}')
