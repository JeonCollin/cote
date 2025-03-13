# import sys

# sys.stdin = open("C:\\Users\\SSAFY\\Downloads\\input.txt", 'r')

T = int(input())

for t in range(1, T+1):
    
    # N개의 매매가
    N = int(input())
    
    products = list(map(int, input().split()))
    
    # 뒤에서부터 자기보다 작은 놈들을 세면 된다
    # 자기보다 큰 놈이 나올 때 까지
    # 자기 번호 - 작은놈들 번호
    profit = 0
    idx = N-1
    i = 1
    
    while True:
        
        # 자기보다 작다면 이익을 낼 수 있다
        if(products[idx-i] < products[idx]):
            profit += products[idx] - products[idx-i]
            i += 1
        
        # 자기보다 크면 그곳으로 인덱스를 바꾼다
        else:
            idx = idx - i
            i = 1
        
        # 종료조건: 인덱스가 0보다 작아짐
        if(idx - i < 0):
            break
        
    
    print(f'#{t} {profit}')