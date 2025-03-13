def decoding(num):

    if(num == '0001101'):
        return '0'
    elif(num == '0011001'):
        return '1'
    elif(num == '0010011'):
        return '2'
    elif(num == '0111101'):
        return '3'
    elif(num == '0100011'):
        return '4'
    elif(num == '0110001'):
        return '5'
    elif(num == '0101111'):
        return '6'
    elif(num == '0111011'):
        return '7'
    elif(num == '0110111'):
        return '8'
    elif(num == '0001011'):
        return '9'

T = int(input())

for t in range(1, T+1):

    # N x M 행렬을 받는다
    N, M = list(map(int, input().split()))

    myarr = [list(input()) for _ in range(N)]

    # 행렬을 순회하며 쓸모 없는 부분을 쳐낸다
    for i in range(N):

        # 0000... 쓸모없다
        # 쓸모 있는 부분만 추출하자
        if(myarr[i] != ['0']*M):
            temp = myarr[i]
            break


    # temp: 0000 암호 0000
    # 끝점 찾기: 뒤에서부터 접근해서 1을 찾자
    for j in range(M-1, 0, -1):
        if(temp[j] == '1'):
            end = j
            break

    # 시작점 찾기: 끝 점 인덱스 - 55
    start = end - 55

    # 암호 해독
    result = ''
    for k in range(start, end+1, 7):

        word = ''
        # 7자리씩 나눈다
        for l in range(7):
            word += temp[k+l]

        # 임시 단어 생성
        # 결과를 해독하고 넣자
        result += decoding(word)



    # 결과 단어 생성
    # 유효 결과인지 확인
    odd = 0
    even = 0
    sumn = 0
    ans = 0

    for index in range(0, len(result), 2):
        even = int(result[index+1])
        odd = int(result[index])

        sumn += odd*3 + even
        ans += even + odd


    # 10의 배수면 정확한 코드: 값 그대로 출력
    if(sumn%10 == 0):
        print(f'#{t} {ans}')

    # 아니면 0 출력 
    else:
        print(f'#{t} 0')

    

