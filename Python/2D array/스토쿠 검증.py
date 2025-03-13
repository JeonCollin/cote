#1~9 합은 45
#1~9 곱은 362880
S = 45
M = 362880

def test_3by3(arr):

    global S
    global M
    sum = 0
    mul = 1

    for i in range(3):
        for j in range(3):
            sum += arr[i][j]
            mul *= arr[i][j]

    #1부터 9까지 다 있다면 1출력
    if(sum == S and mul == M):
        return 1
    
    #겹치는게 하나라도 있다면 0출력
    return 0

def test_1by9(arr):
    global S
    global M
    sum = 0
    mul = 1

    for i in range(9):
        sum += arr[i]
        mul *= arr[i]

    #1부터 9까지 다 있다면 1출력
    if(sum == S and mul == M):
        return 1
    
    #겹치는게 하나라도 있다면 0출력
    return 0




T = int(input())

########### main ############
for t in range(1, T+1):
    
    myarr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    #3by3 검사: 0 3 6
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            #파라미터 초기화
            sample33 = [[0]*3 for _ in range(3)]

            #3by3 샘플조각 만들기
            for k in range(3):
                for l in range(3):
                    sample33[k][l] = myarr[i+k][j+l]

            #결과를 누적해가자
            result = result and test_3by3(sample33)

    #1by9검사
    for idx in range(9):
        #19: 가로, 91: 세로
        sample19 = [0]*9
        sample91 = [0]*9

        #1by9 샘플조각 만들기
        for i in range(9):
            #가로조각
            sample19[i] = myarr[idx][i]

            #세로조각
            sample91[i] = myarr[i][idx]

        result = result and test_1by9(sample19) and test_1by9(sample91)
                
    print(f'#{t} {result}')