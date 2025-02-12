def is_in(str1, str2):

    #str2가 기준 문자열
    for i in range(len(str2)-len(str1) + 1):

        #변수초기화
        same = 0

        #str1이 찾아야 할 문자열
        for j in range(len(str1)):

            if(str1[j] == str2[i+j]):
                same += 1

        #같은 문자열이 있다면 1 출력
        if(same == len(str1)):
            return 1
    
    #아니면 0 출력
    return 0
T = int(input())

for t in range(1, T+1):

    str1 = input()
    str2 = input()

    print(f'#{t} {is_in(str1, str2)}')
