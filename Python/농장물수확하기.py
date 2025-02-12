def count_profit(data):

    #파라미터 초기화
    profit = 0
    length = len(data)
    mid = length//2

    #방향벡터: 좌, 본인, 우

    for row in range(length):
        #점점 커지는 부분
        if(row <= mid):
            for col in range(mid - row, mid + row + 1):
                profit += data[row][col]

        #점점 작아지는 부분
        if(row > mid):
            for col in range(mid - (length-1) + row, mid + (length-1) - row + 1):
                profit += data[row][col]

    return profit

T = int(input())

for t in range(1, T+1):

    N = int(input())

    #농작물 2차원배열
    harvest = [list(map(int, input())) for _ in range(N)]

    #결과출력
    print(f'#{t} {count_profit(harvest)}')