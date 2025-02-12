def write_word(arr, N, K):

    cnt = 0

    #배열을 순회하며 길이가 정확히 3인 곳을 찾아보자
    for i in range(N):

        length_row = 0
        length_col = 0

        for j in range(N):

            #가로
            #가로가 흰색이라면 더해감
            if(arr[i][j] == 1):
                length_row += 1
            
            #가로가 검은색이라면
            #그 전까지 길이가 K인지 확인하고
            #다시 초기화
            elif(arr[i][j] == 0 and length_row == K):
                cnt += 1
                length_row = 0

            elif(arr[i][j] == 0):
                length_row = 0


            #세로
            #세로가 흰색이라면 더해감
            if(arr[j][i] == 1):
                length_col += 1
            
            #세로가 검은색이라면
            #그 전까지 길이가 K인지 확인하고
            #다시 초기화
            elif(arr[j][i] == 0 and length_col == K):
                cnt += 1
                length_col = 0

            elif(arr[j][i] == 0):
                length_col = 0


            #한 구역을 완주

        #최종적으로도 길이가 K라면 횟수에 더한다
        if(length_col == K):
            cnt += 1

        if(length_row == K):
            cnt += 1

    return cnt
            


T = int(input())

for t in range(1, T+1):

    # N:세로길이, K:단어길이
    N, K = list(map(int,input().split()))

    #퍼즐 입력: 1흰, 0검
    puzzle = [list(map(int,input().split())) for _ in range(N)]

    #결과출력
    print(f'#{t} {write_word(puzzle, N, K)}')