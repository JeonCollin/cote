# 좌 > 현재 > 우 순회
def order(n):
    global i

    # 현재 큐에 원소가 없다면
    # 원소를 적는다
    if(0 < n <= N):
        # 좌
        order(2*n)
        # 현재
        tree[n] = i
        i += 1
        # 우
        order(2*n+1)


T = int(input())

for t in range(1, T+1):

    # 1 ~ N 까지의 숫자
    N = int(input())

    tree = [0]*(N+2)
    root = 1
    rear = 0
    i = 1

    order(1)
    # print(tree)
    # 결과 출력
    print(f'#{t} {tree[root]} {tree[N//2]}')