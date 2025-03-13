#달팽이
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

        #행렬 끝 범위에 도달하면 값을 저장하고 방향을 튼다
        if((row == 0 and col == N-1) or (row == N-1 and col == N-1) or (row == N-1 and col == 0)):
            data[row][col] = num
            i+= 1

        #현재 값이 0이라면 숫자 대입
        elif(data[row][col] == 0):
            data[row][col] = num

        #0이 아니라면 한 턴 빼고 방향을 튼다
        else:
            row -= drow[i]
            col -= dcol[i]
            i += 1
            data[row][col] = num
            

        #인덱스가 범위를 벗어나면 초기화
        if(i == 4):
            i = 0

        row += drow[i]
        col += dcol[i]

        num += 1

        if(num == N**2 + 1):
            return data

T = int(input())

for t in range(1, T+1):

    N = int(input())

    #빈 리스트 생성
    mylist = [[0]*N for _ in range(N)]

    snailList = snail(mylist, N)

    for r in range(N):
        print(snailList[r])

