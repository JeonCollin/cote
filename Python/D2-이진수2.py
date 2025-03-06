def float_bin(num):
    # 2를 곱하면서
    # 소수점이 1을 초과하면 이진수는 1
    # 그러고 나서 1을 빼고 다시 곱한다
    # 언제까지? 0이 될 때 까지

    result = ''

    while True:
        
        # 일단 2를 곱한다
        num = num * 2

        # 1이상이 되면 
        # 이진수에 기록하고
        # 1을 뺀다
        if(num >= 1):
            result += '1'
            num = num - 1

            # 만약 소수점이 0이라면 리턴한다
            if(num == 0):
                return result
        
        # 2를 곱해도 1보다 작다면
        # 그 부분 이진수는 0 임
        else:
            result += '0'

        # 13자리 이상이면 오버플로우
        if(len(result) > 12):
            return 'overflow' 

T = int(input())

for t in range(1,T+1):

    num = float(input())

    # 결과 출력
    print(f'#{t} {float_bin(num)}')