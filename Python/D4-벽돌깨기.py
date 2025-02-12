T = int(input())

for t in range(1, T+1):

    #N 
    N, W, H = list(map(int, input().split()))

    #배열 받기
    brick = [list(map(int, input().split())) for _ in range(H)]

    print(f'#{t} {result}')