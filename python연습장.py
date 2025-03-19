def dup_permutation(idx):
    global num
    global N
    global M
    global can_stop

    # 중간에 숫자가 100만을 넘으면 끝낸다
    if(num >= 1000000 or num >= 2*M):
        return
    
    if(idx == cnt):
        # 순열 완성
        # print(num)
        # M이 되면 끝
        if(num == M):
            can_stop = True
            return
        
    else:
        for i in range(4):
            # 해당 연산 수행
            # +1
            if(operators[i] == 0):
                num += 1
            # -1
            elif(operators[i] == 1):
                num -= 1
            # *2
            elif(operators[i] == 2):
                num *= 2
            # -10
            else:
                num -= 10
            P[idx] = operators[i]
            dup_permutation(idx+1)
            if(operators[i] == 0):
                num -= 1
            # -1
            elif(operators[i] == 1):
                num += 1
            # *2
            elif(operators[i] == 2):
                num //= 2
            # -10
            else:
                num += 10
            

T = int(input())

for t in range(1, T+1):
    
    # N: 현재 수, M: 원하는 수
    N, M = list(map(int, input().split()))
    
    # +1, -1, *2, -10 
    operators = [0,1,2,3]
    cnt = 1
    num = N
    can_stop = False
    
    # 연산에 대한 중복순열을 생성한다
    # 한 칸씩 늘려가며 모든 조합을 살핀다
    while True:
        P = [0]*cnt
        dup_permutation(0)
        
        # M이 되면 멈춘다
        if(can_stop == True):
            break
        
        cnt += 1

    
    # 결과 출력
    print(f'#{t} {cnt}')