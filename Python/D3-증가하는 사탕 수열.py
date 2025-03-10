def eat(a, b, c):
    # 사탕을 먹어치워서 오름차순으로 만든다
    
    # 근데 마지막 사탕이 2개 이하라면 불가능
    # 두 번째 사탕이 1개 이하라면 불가능
    if(c <= 2 or b <= 1):
        return -1
    
    # 최소한 먹어야 하는 횟수
    cnt = 0
    
    # 마지막 사탕보다 적을 때 까지 두 번째 사탕을 먹어치운다
    while(b >= c):
        b = b - 1
        cnt += 1
        
    # 두 번째 사탕보다 적을 때 까지 첫 번째 사탕을 먹는다
    while(a >= b):
        a = a - 1
        cnt += 1
        
    return cnt
    

T = int(input())

for t in range(1, T+1):
    
    # A, B, C 개의 사탕
    A, B, C = list(map(int, input().split()))
    
    print(f'#{t} {eat(A, B, C)}')