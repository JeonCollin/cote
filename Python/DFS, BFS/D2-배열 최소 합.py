def permutation(i, N):
    global min

    if(i == N):
        # 순열 완성
        # 합을 구하고 최대인지 비교하자
        sum = 0
        for n in range(N):
            sum += mylist[n][P[n]]

        if(sum <= min):
            min = sum
        return

    else:
        # i부터 시작해서 j와 바꾸면서 순열을 끼워맞추자
        for j in range(i, N):
            # i와 j를 바꿈
            P[i], P[j] = P[j], P[i]
            permutation(i+1, N)
            # 원상복구
            P[i], P[j] = P[j], P[i]



T = int(input())

for t in range(1, T+1):

    # N: 행렬 크기
    N = int(input())

    mylist = [list(map(int, input().split())) for _ in range(N)]

    # 행에대한 순열을 생성하자
    P = [i for i in range(N)]
    min = 10*N

    permutation(0, N)

    print(f'#{t} {min}')
