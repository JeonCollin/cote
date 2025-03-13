def is_palindrome(alpha_list, L):
    #회문인지 아닌지 검사하는 함수
    #특정 문자열을 받아서 앞뒤로 비교한다

    for i in range(L):

        #회문이 아니라면 false 반환
        if(alpha_list[i] != alpha_list[L-1 - i]):
            return False
        
    #회문이라면 true 반환
    return True

def arr_to_word(myarr, L):
    #배열을 받아 L 줄의 글자로 바꿔주는 함수
    #그 후 팰린드롬 검사도 한다
    cnt = 0

    #arr를 순환한다
    for i in range(8):
        for j in range(8-L + 1):
            arr_row = ['']*L
            arr_col = ['']*L

            for l in range(L):
                #가로 샘플링
                arr_row[l] = myarr[i][j+l]
                #세로 샘플링
                arr_col[l] = myarr[j+l][i]

            if(is_palindrome(arr_row, L) == True):
                cnt += 1

            if(is_palindrome(arr_col, L) == True):
                cnt += 1

    return cnt


for t in range(10):

    #회문 길이
    L = int(input())

    #글자배열 받기
    arr = [list(input()) for _ in range(8)]

    #결과출력
    print(f'#{t+1} {arr_to_word(arr, L)}')