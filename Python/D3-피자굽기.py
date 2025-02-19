def isEmpty():
    return front == rear

def isFull():
    return front == (rear+1) % L

def enqueue(item):
    global rear

    if(isFull() == True):
        print('full')

    else:
        rear = (rear+1) % L
        queue[rear] = item

def dequeue():
    global front

    if(isEmpty() == True):
        print('empty')

    else:
        front = (front+1) % L
        return queue[front]
    

def last_pizza(cheese_list, pizza_list):
    global N
    global M
    global L

    # 피자(인덱스)를 큐에 넣는다
    # cheese_list[피자] == 치즈 양
    for i in range(N):
        enqueue(i)

    # 꺼낸 피자 갯수
    cnt = 0
    # 피자 예비 번호
    rest_pizza = N

    while True:

        # 피자 하나를 꺼내서 확인한다
        # 절반으로 줄어든 상태일거다
        pizza = dequeue()
        cheese_list[pizza] = cheese_list[pizza] // 2

        # 치즈가 덜 녹은 경우
        if(cheese_list[pizza] != 0):
            # 다시 굽는다
            enqueue(pizza)

        # 치즈가 다 녹은 경우
        else:

            # 완성된 피자 수 증가
            cnt += 1
            # 꺼낸 피자 기록
            pizza_list[pizza] = 0

            # 최후의 1인이 남았으면 결과 리턴
            if(cnt == M-1):
                return pizza_list
            
            #아직 남은 피자가 있으면 넣는다
            elif(rest_pizza < M):
                enqueue(rest_pizza)
                rest_pizza += 1

T = int(input())

for t in range(1, T+1):
    
    # N: 화덕의 크기, M:피자 개수
    N, M = list(map(int, input().split()))

    # M개 피자에 뿌려진 치즈 양, 피자 리스트
    cheese_list = list(map(int, input().split()))
    pizza_list = [1]*M

    # 원형 큐: 들어갈 수 있는 피자 양+1 로 생성
    L = N + 1
    queue = [0]*L
    front = 0
    rear = 0

    result = last_pizza(cheese_list, pizza_list)

    # 결과출력: 1로 있는 아이 +1 해야 원래 피자임
    print(f'#{t} {result.index(1) + 1}')