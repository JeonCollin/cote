def snail(data, N):

    #우 하 좌 상
    drow = [0, 1,  0, -1]
    dcol = [1, 0, -1,  0]

    #초기화
    num = 1
    i = 0
    row = 0
    col = 0

    while True:

        #행렬 범위 내에서
        if(0 <= row < N and 0 <= col < N):

            #현재 값이 0이라면 숫자 대입
            if(data[row][col] == 0):
                data[row][col] = num

            #0이 아니라면 방향을 튼다
            else:
                i += 1

        #인덱스가 범위를 벗어나면 초기화
        if(i == 4):
            i = 0

        row += drow[i]
        col += dcol[i]

        num += 1

        if(num == 101):
            return data

T = int(input())

for t in range(1, T+1):

    N = int(input())

    #빈 리스트 생성
    mylist = [[0]*N for _ in range(N)]

    snailList = snail(mylist, N)

    for r in range(N):
        print(snailList[r])
