def palindrome(string, M):
    #글자를 받아서 회문인지 검사함

    #문자열의 맨 앞과 맨 끝부터 비교한다
    #한 글자라도 다르면 False 반환
    for i in range(M):
        if(string[i] != string[M-1 - i]):
            return False
    
    #회문일경우 True 반환
    return True


T = int(input())

for t in range(1, T+1):

    #N by N, 길이가 M인 회문
    N, M = list(map(int, input().split()))

    #문자행렬 받음
    arr = [list(input()) for _ in range(N)]

    #변수초기화
    mylist = []
    pal = ''

    #가로 검사
    for row in range(N):
        for col in range(N-M+1):
            
            #M글자를 생성한다
            for i in range(M):
                mylist += arr[row][col+i]

            #가로로 M글자가 회문인지 확인한다
            if(palindrome(mylist, M) == True):
                pal = ''.join(mylist)

            #글자 초기화
            mylist = []

    #세로 검사
    for col in range(N):
        for row in range(N-M+1):

            #M글자를 생성한다
            for i in range(M):
                mylist += arr[row+i][col]

            #세로로 M글자가 회문인지 확인한다
            if(palindrome(mylist, M) == True):
                pal = ''.join(mylist)

            #글자 초기화
            mylist = []

    #결과출력
    print(f'#{t} {pal}')