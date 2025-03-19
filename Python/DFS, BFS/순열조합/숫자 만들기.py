'''
2, 2, 2, 2개의 연산자라면
8C2 x 6C2 x 4C2 x 2C2
'''

def combination_plus(idx, start):
    global C
    # 모든 plus 소진
    if(idx == num_plus):
        # print(C)
        # minus를 빈공간에 채운다
        combination_minus(0,0)
        
    # plus가 들어갈 자리를 선택한다
    else:
        for i in range(start, N-1):
            C[i] = 1
            combination_plus(idx+1, i+1)
            C[i] = 0

def combination_minus(idx, start):
    global C
    
    if(idx == num_minus):
        combination_multiply(0,0)
        
    else:
        for i in range(start, N-1):
            if(C[i] == 0):
                C[i] = 2
                combination_minus(idx+1, i+1)
                C[i] = 0

def combination_multiply(idx, start):
    global C
    
    if(idx == num_muliply):
        combination_divide(0,0)
        
    else:
        for i in range(start, N-1):
            if(C[i] == 0):
                C[i] = 3
                combination_multiply(idx+1, i+1)
                C[i] = 0

def combination_divide(idx, start):
    global C
    global numbers
    global result
    
    if(idx == num_divide):
        # 최종 순열 완성
        # 순열을 순회하며 해당하는 연산을 수행한다
        num = numbers[0]
        
        for n in range(N-1):
            # plus
            if(C[n] == 1):
                num += numbers[n+1]
            # minus
            elif(C[n] == 2):
                num -= numbers[n+1]
            # multiply
            elif(C[n] == 3):
                num *= numbers[n+1]
            # divide
            else:
                num = int(num/numbers[n+1])
        
        # 결과 저장
        result.append(num)
        
    else:
        for i in range(start, N-1):
            if(C[i] == 0):
                C[i] = 4
                combination_divide(idx+1, i+1)
                C[i] = 0

T = int(input())

for t in range(1, T+1):
    
    # 숫자 갯수
    N = int(input())
    
    # + - * //
    num_operaters = list(map(int, input().split()))
    
    num_plus = num_operaters[0]
    num_minus = num_operaters[1]
    num_muliply = num_operaters[2]
    num_divide = num_operaters[3]
    
    # 수식에 사용되는 숫자
    numbers = list(map(int, input().split()))
    
    C = [0]*(N-1)
    result = []
    
    combination_plus(0,0)
    # print(result)
    
    # 결과 출력
    print(f'#{t} {max(result) - min(result)}')