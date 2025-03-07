def decoding(second, third, forth):
    # 첫 번째 자리는 그리 안중요
    m = 1

    while True:
        second = second//m
        third = third // m
        forth = forth // m
    if((second == 2 and third == 1 and forth == 1) or
       (second == 4 and third == 2 and forth == 2) or
       (second == 6 and third == 3 and forth == 3) or
       (second == 8 and third == 4 and forth == 4) or
       (second == 10 and third == 5 and forth == 5) or
       (second == 12 and third == 6 and forth == 6)):
        return '0'
    
    elif((second == 2 and third == 2 and forth == 1) or
         (second == 4 and third == 4 and forth == 2) or
         (second == 6 and third == 6 and forth == 3) or
         (second == 8 and third == 8 and forth == 4) or
         (second == 10 and third == 10 and forth == 5) or
         (second == 12 and third == 12 and forth == 6)):
        return '1'
    
    elif((second == 1 and third == 2 and forth == 2) or
         (second == 2 and third == 4 and forth == 4) or
         (second == 3 and third == 6 and forth == 6) or
         (second == 4 and third == 8 and forth == 8) or
         (second == 5 and third == 10 and forth == 10) or
         (second == 6 and third == 12 and forth == 12)):
        return '2'
    
    elif((second == 4 and third == 1 and forth == 1) or
         (second == 8 and third == 2 and forth == 2) or
         (second == 12 and third == 3 and forth == 3) or
         (second == 16 and third == 4 and forth == 4) or
         (second == 20 and third == 5 and forth == 5) or
         (second == 24 and third == 6 and forth == 6)):
        return '3'
    
    elif((second == 1 and third == 3 and forth == 2) or
         (second == 2 and third == 6 and forth == 4) or
         (second == 3 and third == 9 and forth == 6) or
         (second == 4 and third == 12 and forth == 8) or
         (second == 5 and third == 15 and forth == 10) or
         (second == 6 and third == 18 and forth == 12)):
        return '4'
    
    elif((second == 2 and third == 3 and forth == 1) or 
         (second == 4 and third == 6 and forth == 2) or
         (second == 6 and third == 9 and forth == 3) or
         (second == 8 and third == 12 and forth == 4) or
         (second == 10 and third == 15 and forth == 5) or
         (second == 12 and third == 18 and forth == 6)):
        return '5'
    
    elif((second == 1 and third == 1 and forth == 4) or
         (second == 2 and third == 2 and forth == 8) or
         (second == 3 and third == 3 and forth == 12) or
         (second == 4 and third == 4 and forth == 16) or
         (second == 5 and third == 5 and forth == 20) or
         (second == 6 and third == 6 and forth == 24)):
        return '6'
    
    elif((second == 3 and third == 1 and forth == 2) or 
         (second == 6 and third == 2 and forth == 4) or
         (second == 9 and third == 3 and forth == 6) or
         (second == 12 and third == 4 and forth == 8) or
         (second == 15 and third == 5 and forth == 10) or
         (second == 18 and third == 6 and forth == 12)):
        return '7'
    
    elif((second == 2 and third == 1 and forth == 3) or 
         (second == 4 and third == 2 and forth == 6) or
         (second == 6 and third == 3 and forth == 9) or
         (second == 8 and third == 4 and forth == 12) or
         (second == 10 and third == 5 and forth == 15) or
         (second == 12 and third == 6 and forth == 18)):
        return '8'
    
    elif((second == 1 and third == 1 and forth == 2) or 
         (second == 2 and third == 2 and forth == 4) or
         (second == 3 and third == 3 and forth == 6) or
         (second == 4 and third == 4 and forth == 8) or
         (second == 5 and third == 5 and forth == 10) or
         (second == 6 and third == 6 and forth == 12)):
        return '9'

def hex_to_bin(item):

    if(item == '0'):
        return '0000'
    elif(item == '1'):
        return '0001'
    elif(item == '2'):
        return '0010'
    elif(item == '3'):
        return '0011'
    elif(item == '4'):
        return '0100'
    elif(item == '5'):
        return '0101'
    elif(item == '6'):
        return '0110'
    elif(item == '7'):
        return '0111'
    elif(item == '8'):
        return '1000'
    elif(item == '9'):
        return '1001'
    elif(item == 'A'):
        return '1010'
    elif(item == 'B'):
        return '1011'
    elif(item == 'C'):
        return '1100'
    elif(item == 'D'):
        return '1101'
    elif(item == 'E'):
        return '1110'
    elif(item == 'F'):
        return '1111'


import sys
sys.stdin = open("C:\\Users\\SSAFY\\Downloads\\sample_input(3).txt", 'r')


T = int(input())

for t in range(1, T+1):

    # N x M 행렬을 받는다
    N, M = list(map(int, input().split()))

    myarr = [list(input()) for _ in range(N)]

    # 정답 초기화
    ans = 0
    ans_list = []
    row = 1

    # 행렬을 순회하며 쓸모 없는 부분을 쳐낸다
    for i in range(N):

        # 일단 유효한 부분의 중복을 없앤다
        for j in range(M-1):
            if(myarr[i][j] != '0'):
                while True:
                    
                    # 아래도 똑같다면 다 지워버린다
                    if(myarr[i][j] == myarr[i+row][j] and myarr[i][j+1] == myarr[i+row][j+1]):
                        myarr[i+row][j] = '0'
                        myarr[i+row][j+1] = '0'
                        row += 1

                    # 다른 수(0)이 나온다면 끝낸다
                    else:
                        row = 1
                        break

####

    # 행렬을 순회하며 쓸모 없는 부분을 쳐낸다
    for i in range(N):

        # 0000... 쓸모없다
        # 쓸모 있는 부분만 추출하자
        if(myarr[i] == ['0']*M):
            continue

        # 쓸모 있는 부분 생성
        temp = ''

        # 쓸모 있는 부분을 16진수 >> 2진수로 바꾸자
        for j in range(M):
            temp += hex_to_bin(myarr[i][j])

        # 0011100011 0으로 마지막 1이 제외되는 경우 제거
        temp = temp + '00' #?

        # print('쓸모:', temp)
####

        # 처음 부터 끝 까지 비트에서 1의 개수와 0의 개수를 찾자
        # 번갈아 가면서 해보자
        cnt0 = 0
        cnt1 = 0
        partial = []

        for k in range(len(temp)-1):
            
            # 현재 비트가 0이면
            if(temp[k] == '0'):

                # 0의 개수 증가
                cnt0 += 1

                # 다음비트가 1이면 지금까지 나온 0의 개수 기록, 초기화
                if(temp[k+1] == '1'):
                    partial.append(cnt0)
                    cnt0 = 0

            # 현재 비트가 1이면
            else:

                # 1의 개수 증가
                cnt1 += 1

                # 다음비트가 0이면 지금까지 나온 1의 개수 기록, 초기화
                if(temp[k+1] == '0'):
                    partial.append(cnt1)
                    cnt1 = 0

        #print('01비율:',partial)

####

        # 0과 1의 비율이 번갈아가면서 생성됨
        # 그럼 이제 4칸씩 나눠서 해당하는 숫자를 뽑아내자
        numbers = ''

        for l in range(0, len(partial), 4):

            # 1. 0의 개수(이거는 안중요함) >> 0이 연속으로 있는 구간이 있기 때문
            first0 = partial[l]
            # 2. 1의 개수
            second1 = partial[l+1]
            # 3. 0의 개수
            third0 = partial[l+2]
            # 4. 1의 개수
            forth1 = partial[l+3]

            # 그 비율에 해당하는 수를 찾아내자
            numbers += decoding(second1, third0, forth1)

        #print(numbers)
####
        # 수를 찾아냈으면 계산하자
        odd =  0
        even = 0
        check_sum = 0
        just_sum = 0
        max_sum = 0
        

        # 근데 끊어서 계산해야 한다 >> 한 줄에 여러 암호가 있을 수도 있다.
        for m in range(0, len(numbers), 8):

            # 8개로 끊은 숫자 생성
            divided_num = (numbers[m] + numbers[m+1] + numbers[m+2] + numbers[m+3] +
                            numbers[m+4] + numbers[m+5] + numbers[m+6] + numbers[m+7])
            
            for n in range(0, len(divided_num), 2):
                odd = int(numbers[n])
                even = int(numbers[n+1])

                check_sum += 3*odd + even
                just_sum += odd + even

####
            # 정상적인 암호의 그냥 합을 저장한다
            if(check_sum%10 == 0):
                ans = just_sum
                ans_list.append(just_sum)

    # 결과 출력
    print(f'#{t} {sum(ans_list)}')    
    

