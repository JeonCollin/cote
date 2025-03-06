def enq(item):
    global rear
    global root

    # 일단 rear 증가
    rear += 1

    # heap에 넣고 본다
    heap[rear] = item

    # parents node, child node 생성
    c = rear
    p = c//2

    # parent가 root가 될 때 까지 로테이션 진행
    # 최대 heap이니까 작은 것들이 아래로 가야 함
    while(p >= root):
        
        # 아래 자식들이랑 크기 비교
        # parent가 left보다 작고
        # left가 right보다 크다면 교체
        if(heap[p] < heap[c]):
            heap[p], heap[c] = heap[c], heap[p]

        # 위의 level로 parent 이동
        c = p
        p = p //2

def deq():
    global rear
    global root

    # 일단 root에서 원소를 꺼낸다
    temp = heap[root]

    # 마지막 원소를 root에 집어 넣는다
    # 그러고 나서 rear를 앞으로 한 칸 당긴다
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1

    # 더이상 원소가 없다면 -1 리턴
    if(rear == -1):
        rear = 0
        return -1

    # 이제 다시 로테이션 해야 함
    # deq는 위에서부터 내려가야 할 것 같다
    p = 1
    c = 2*p

    # 로테이션 적용
    while(c <= rear):

        # 오른쪽에 자식이 존재한다면
        if(c+1 <= rear and heap[c] < heap[c+1]):
            # 비교 대상을 오른쪽으로 한다
            c += 1

        # 자식이 더 크다면
        if(heap[p] < heap[c]):
            # 교환
            heap[p], heap[c] = heap[c], heap[p]

        # 아래 level로 parent 이동
        p = c
        c = 2*p

    # 로테이션 끝났으면 root 리턴
    return temp

T = int(input())

for t in range(1, T+1):

    # 수행하는 연산 수
    N = int(input())

    # heap 초기화
    # 최대 힙
    heap = [0]*(N+2)
    root = 1
    rear = 0

    # 결과용
    result = []

    # 수행하는 연산을 받는다
    # 1 x: x를 삽입
    # 2: 최대 값 출력 후 삭제
    for n in range(N):

        order = list(map(int, input().split()))

        # 1: 삽입
        if(order[0] == 1):
            enq(order[1])

        # 2: 삭제
        else:
            result.append(deq())

        # print(heap)

    # 결과출력
    print(f'#{t} {" ".join(map(str, result))}')