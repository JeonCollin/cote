'''
1. 하루 가격으로 더해간다 day+
2. 한 달 가격이랑 비교한다 month <> day
3. 달 별로 하루/한달 최적의 가격을 선정한다
4. 1~3달까지는 최적 가격을 직접 구한다
5. 4달 이후로 최적의 가격: An = An-1 + an or An-3 + qn-2
6. A12 와 1년 요금의 크기 비교
'''

def lowest_cost():
    global a
    global q
    
    cost = [0]*12
        
    # 한 달, 세달을 이용해서 최적의 가격 엄선
    # 첫 달
    cost[0] = a[0]
    
    # 두번째 달
    cost[1] = a[0] + a[1]
    
    # 세 번째 달
    # 한 달 이용권 3개 / 3달 이용권 비교
    if(cost[1] + a[2] > q[1]):
        cost[2] = q[1]
        
    else:
        cost[2] = cost[1] + a[2]
        
    # 4 ~ 11 달
    n = 3
    
    while(n <= 10):
        
        # 이전 최적 + 한 달 / 새로운 3달 + 처음 최적
        if(cost[n-1] + a[n] < cost[n-3] + q[n-2]):
            cost[n] = cost[n-1] + a[n]
            
        else:
            cost[n] = cost[n-3] + q[n-2]
            
        n += 1
            
    # 마지막 12 달
    num1 = cost[10] + a[11] # 50+80=130
    num2 = cost[8] + q[9] # 50+50=100
    
    # 분기가 더 싼 경우
    if(q[10] != 0):
        num3 = cost[9] + q[10] # 50+50 = 100
        
        if(num1 <= num2 and num1 <= num3):
            cost[11] = num1
            
        elif(num2 <= num1 and num2 <= num3):
            cost[11] = num2
        
        elif(num3 <= num1 and num3 <= num2):
            cost[11] = num3
            
    # 한 달이 더 싼 경우
    else:
        if(num1 < num2):
            cost[11] = num1
            
        else:
            cost[11] = num2
            
    # 1년 회원권이랑 비교
    if(cost[11] > price_year):
        cost[11] = price_year
            
    return cost
    

T = int(input())

for t in range(1, T+1):
    
    # 1일, 1달, 3달, 1년 이용권 요금
    price_day, price_month, price_quater, price_year = list(map(int, input().split()))
    
    # 1 ~ 12개월 이용 계획
    plane_year = list(map(int, input().split()))
    
    # 1 ~ 3. 하루 가격과 한 달 가격 중 최적의 리스트: a[n]
    # 하루 이용권만 사용했을 때
    a1 = [0]*12
    for i in range(12):
        a1[i] = price_day*plane_year[i]
    
    # 한 달 이용권만 사용했을 때
    a2 = [0]*12
    for j in range(12):
        # 사용 안하는 달
        if(plane_year[j] == 0):
            a2[j] = 0
        
        # 사용하는 달
        else:
            a2[j] = price_month
    
    # 둘 중 최적의 가격만 선택
    a = [0]*12
    for k in range(12):
        if(a1[k] <= a2[k]):
            a[k] = a1[k]
        
        else:
            a[k] = a2[k]
    
    # 세 달 가격 리스트(n달 ~ n+2달): qn
    q = [price_quater]*10 + [0, 0]
    
    # 마지막 두 달을 뽕뽑을 수 있다면 11항도 추가
    if(a[10] + a[11] > price_quater):
        q[10] = price_quater
        
    
    # print('a:',a)
    # print('q:',q)
    
    # 4 ~ 5.
    # 한 달, 세달을 이용해서 최적의 가격 엄선
    
    optimize = lowest_cost()
    # print('cost:',optimize)
    
    
    print(f'#{t} {optimize[11]}')