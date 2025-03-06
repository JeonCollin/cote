def isEmpty():
    return front == rear

def isFull():
    return front == (rear+1)%9

def enqueue(item):
    global rear

    if(isFull() == True):
        print('full')

    else:
        rear = (rear+1)%9
        queue[rear] = item

def dequeue():
    global front

    if(isEmpty() == True):
        print('empty')

    else:
        front = (front+1)%9
        return queue[front]

def password_cycle():

    cycle = 1

    while True:

        # 한 싸이클을 거친 숫자
        num = dequeue()
        num -= cycle

        # 0보다 크면 cycle 만큼 감소 후 뒤로 이동
        if(num > 0):
            enqueue(num)

        # 0이하면 0을 넣고 끝
        else:
            enqueue(0)
            return
        
        cycle += 1

        # 최대 싸이클은 5임
        if(cycle == 6):
            cycle = 1


for t in range(1, 11):

    T = int(input())

    # 8개의 암호
    password = list(map(int, input().split()))

    # 원형 큐여서 앞에 + 1 해줘야함
    queue = [0] + password
    front = 0
    rear = 8

    password_cycle()

    result = ''

    for i in range(8):
        result += str(dequeue())

    # 결과출력
    print(f'#{t} {" ".join(result)}')