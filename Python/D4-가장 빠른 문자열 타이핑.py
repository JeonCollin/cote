def typing(str1, str2):
    #str1 = A
    #str2 = B

    a = len(str1)
    b = len(str2)

    cnt = 0
    copy = 0

    #기준 문자열:a
    for i in range(a-b+1):
        
        #length 초기화
        length = 0

        #b와 동일한지 확인
        for j in range(b):

            #다르면 끝
            if(str1[i+j] != str2[j]):
                break

            length += 1

        #동일한 문자가 있다면 그 문자열 자체의 길이를 센다
        if(length == b):
            for idx in range(b):
                str1[i+idx] = ''
                copy += 1
            cnt += 1

    #최종 타자 횟수 = 원래 길이 - 중복된 길이 + 나온 횟수
    return a - copy + cnt

    


T = int(input())

for t in range(1, T+1):

    inputlist = list(input().split())
    A = list(inputlist[0])
    B = list(inputlist[1])

    #결과출력
    print(f'#{t} {typing(A, B)}')