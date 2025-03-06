def pre_order(n):
    # 전위 탐색
    global cnt
    # 현재 > 좌 > 우
    # 현재보다 작아지지 않는 곳에서 찾는다
    if(n != 0):
        # 현재
        cnt += 1
        # 좌
        pre_order(left[n])
        # 우
        pre_order(right[n])


T = int(input())

for t in range(1, T+1):

    # E 간선 수, N 노드의 정체
    E, N = list(map(int, input().split()))

    # 간선 정보 받기
    left = [0]*(E+2)
    right = [0]*(E+2)

    mylist = list(map(int, input().split()))

    for e in range(0, 2*E, 2):
        p = mylist[e]
        c = mylist[e+1]

        # left children
        if(left[p] == 0):
            left[p] = c

        # right children
        else:
            right[p] = c

    cnt = 0
    pre_order(N)

    print(f'#{t} {cnt}')
    # print(left)
    # print(right)