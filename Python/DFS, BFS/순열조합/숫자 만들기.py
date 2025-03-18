def calculate():
    global sumn
    global P

    # 초기 값 계산
    if(P[0] == '+'):
        sumn = numbers[0] + numbers[1]

    elif(P[0] == '-'):
        sumn = numbers[0] - numbers[1]

    elif(P[0] == '*'):
        sumn = numbers[0] * numbers[1]

    elif(P[0] == '/'):
        sumn = numbers[0] // numbers[1]

    # 그 뒤로는 계속 누적시킨다
    for i in range(1, N-1):
        if(P[i] == '+'):
            sumn = sumn + numbers[i+1]

        elif(P[i] == '-'):
            sumn = sumn - numbers[i+1]

        elif(P[i] == '*'):
            sumn = sumn * numbers[i+1]

        elif(P[i] == '/'):
            sumn = sumn // numbers[i+1]

    return sumn

def permutation(idx):
    global used
    global operands
    global P

    # 순열이 완성되는 부분
    if(idx == N-1):
        # 조건에 맞춰서 계산한다
        #print(P)
        num_calculate = calculate()
        result.append(num_calculate)
        return
    
    # 순열을 만들어가는 부분
    else:
        # 순열에 수를 넣는다
        for i in range(N-1):
            # 사용하지 않았던 수라면 선택한다
            if(used[i] == 0):
                used[i] = 1
                P[idx] = operands[i]
                permutation(idx+1)
                used[i] = 0


def dup_permutation(translate):
    # 중복순열은
    # 00123을 점점 오름차순으로 정렬하는 것과 같다
    # 00132 00213 ...
    
    # 피벗 포인트 찾기(오른쪽에서 왼쪽으로 i << i + 1)
    i = len(translate) - 2
    while(i >= 0 and translate[i] >= translate[i+1]):
        i -= 1
    pivot = i
    
    # 모두 다 정렬되었다.
    if(pivot < 0):
        return
    
    # 피벗 포인트보다 오른쪽에 위치한 값들 중에서
    # 피벗 값보다 큰 것 들 중 가장 작은 값 찾기
    j = len(translate-1)
    
    # j가 더 뒤에 있고, 더 작다면 그냥 넘긴다
    while(j > pivot and translate[j] <= translate[pivot]):
        j -= 1
        
    translate[pivot], translate[j] = translate[j], translate[pivot]
    
    translate[pivot+1 : ] = reversed(translate[pivot + 1 : ])
    
    return translate
        

T = int(input())

for t in range(1, T+1):

    # 숫자 갯수
    N = int(input())

    #연산자 종류과 개수 받기, 순열 초기화
    num_operands = list(map(int, input().split()))
    P = [0]*(N-1)

    # 연산자 종류대로 나열
    operands = '+'*num_operands[0] + '-'*num_operands[1] + '*'*num_operands[2] + '/'*num_operands[3]
    # translate = '0'*num_operands[0] + '1'*num_operands[1] + '2'*num_operands[2] + '3'*num_operands[3]

    #수식에 사용될 숫자 받기
    numbers = list(map(int, input().split()))

    # 사용 리스트 생성
    used = [0]*(N-1)

    # 변수 초기화
    sumn = 0
    result = []

    # permutation(0)

    #결과 출력   
    print(f'#{t} {max(result) - min(result)}')