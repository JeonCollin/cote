def post_order(n):
    global sumn
    # 후위 순회
    # 좌 > 우 > 현재
    # root 까지 살펴봐야 한다
    if(0 < n <= N):
        # left
        post_order(2*n)
        # right
        post_order(2*n+1)
        # now
        sumn += tree[n]


T = int(input())

for t in range(1, T+1):

    # N 노드의 개수, M 리프 노드의 개수, L 값을 출력할 노드 번호
    N, M, L = list(map(int, input().split()))

    # 루트가 1인 완전 트리를 만들자
    tree = [0]*(N+1)
    
    # M번 동안 리프노드 번호와 자연수가 주어짐
    for m in range(M):
        idx, num = list(map(int, input().split()))

        # leaf에 저장
        tree[idx] = num

    sumn = 0

    post_order(L)

    # 결과 출력
    print(f'#{t} {sumn}')