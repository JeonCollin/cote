def find_start(data, start_row, start_col):

    #파라미터 초기화
    row = start_row
    col = start_col

    while(0 <= row < 100 and 0 <= col < 100):
        
        #그냥 지나가면 왼쪽1과 오른쪽1이 충돌이 일어남
        #그래서 지나간 자리는 0으로 초기화 해야함
        #우선순위1: 왼쪽(오른쪽)
        if(col-1 >= 0 and data[row][col-1] == 1):
            data[row][col] = 0
            col = col - 1

        #우선순위2: 오른쪽(왼쪽)
        elif(col+1 < 100 and data[row][col+1] == 1):
            data[row][col] = 0
            col = col + 1
        
        #우선순위3: 위쪽
        elif(row-1 >= 0 and data[row-1][col] == 1):
            data[row][col] = 0
            row = row - 1

        if(row == 0):
            return col
        


#총 10개의 테스트케이스가 주어진다
for t in range(1, 11):

    T = int(input())

    #파라미터 초기화
    N = 100
    end_row = 99
    end_col = 0

    #사다리 받기
    ladder = [list(map(int, input().split())) for _ in range(N)]

    #도착지점 찾아놓기
    for j in range(N):
        if(ladder[99][j] == 2):
            end_col = j

    #알고리즘, 결과출력
    print(f'#{t} {find_start(ladder, 99, end_col)}')
    