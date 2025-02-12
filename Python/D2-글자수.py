def best_word(string1, string2):
    #string1이 짧은 문자열, string2가 긴 문자열
    N = len(string1)
    M = len(string2)

    #최대값 초기화
    max = 0

    #짧은 문자가 기준
    for i in range(N):

        num = 0

        #긴 문자열을 순회한다
        for j in range(M):
            
            if(string1[i] == string2[j]):
                num += 1
        
        #최대값 갱신
        if(max <= num):
            max = num

    return max

T = int(input())

for t in range(1, T+1):

    #str1이 짧은 문자열, str2가 긴 문자열
    str1 = input()
    str2 = input()

    #결과출력
    print(f'#{t} {best_word(str1, str2)}')