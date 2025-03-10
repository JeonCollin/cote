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

    while True:
        pass
        

T = int(input())

for t in range(1, T+1):

    # 숫자 갯수
    N = int(input())

    #연산자 종류과 개수 받기, 순열 초기화
    num_operands = list(map(int, input().split()))
    P = [0]*(N-1)

    # 연산자 종류대로 나열
    operands = '+'*num_operands[0] + '-'*num_operands[1] + '*'*num_operands[2] + '/'*num_operands[3]
    translate = '0'*num_operands[0] + '1'*num_operands[1] + '2'*num_operands[2] + '3'*num_operands[3]

    #수식에 사용될 숫자 받기
    numbers = list(map(int, input().split()))

    # 사용 리스트 생성
    used = [0]*(N-1)

    # 변수 초기화
    sumn = 0
    result = []

    permutation(0)

    #결과 출력
    print(f'#{t} {max(result) - min(result)}')