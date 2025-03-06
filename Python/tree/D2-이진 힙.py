def enq(item):
    # 최소 힙
    global root
    global heap
    global rear

    # 일단 rear 증가
    rear += 1

    # 힙에 저장
    heap[rear] = item

    # 부모, 자식 선언
    c = rear
    p = c//2

    # 최소가 루트로 오도록 정리하자
    # 부모가 루트에 도달할 때 까지
    while(p >= root):

        # parent가 left child보다 큰 경우
        # left child가 0이 아니여야 함
        if(heap[2*p] != 0 and heap[p] > heap[2*p]):
            # 바꾼다
            heap[p], heap[2*p] = heap[2*p], heap[p]

        # right child도 마찬가지
        if(heap[2*p+1] != 0 and heap[p] > heap[2*p+1]):
            # 바꾼다
            heap[p], heap[2*p+1] = heap[2*p+1], heap[p]

        # 비교 노드를 한 칸 올리자
        p = p // 2

        # print(heap)

def add_josang(n):
    # root까지 거슬러 올라가며 합을 더함
    # n은 현재 노드
    global sum

    # 루트까지 거슬러간다
    if(n != 0):
        sum += heap[n]
        # 그 다음 조상
        add_josang(n//2)



T = int(input())

for t in range(1, T+1):

    N = int(input())

    # heap 초기화
    heap = [0]*(N+2)
    root = 1
    rear = 0

    # 숫자 받자
    num = list(map(int, input().split()))

    # 트리에 숫자를 채운다
    for i in range(N):
        enq(num[i])

    # 마지막 원소에서 조상을 거슬러 가며 더하자
    sum = 0
    add_josang(rear//2)

    # 결과 출력
    print(f'#{t} {sum}')
    # print(heap)