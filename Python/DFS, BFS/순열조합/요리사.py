'''
4개에서 나올 수 있는 조합
(A) B
01
02
03
12
13
23

6개에서 나올 수 있는 조합
(A) B
012 >> [0][1]+[0][2] + [1][0]+[1][2] + [2][0]+[2][1]
013
014
015
023
024
025
034
035
045
123
124
125
134
135
145
234
235
245
345

n 개에서 나올 수 있는 조합
r = n//2
nCr
'''
def combination(idx, start):
    global A, B
    global minn
    global R
    
    if(idx == R):
        # 조합 완성
        # 0: A, 1:B
        # 조합을 순회하며 A와 B를 합한다
        for r in range(N):
            for c in range(N):
                
                # 같은 인덱스는 제외한다
                if(r == c):
                    continue
                
                # A를 더하는 경우
                if(C[r] == 0 and C[c] == 0):
                    A += food_list[r][c]
                    
                # B를 더하는 경우
                if(C[r] == 1 and C[c] == 1):
                    B += food_list[r][c]
        
        # 둘의 차이의 최소값 갱신
        if(minn > abs(A-B)):
            minn = abs(A-B)
            
        # 초기화
        A = 0
        B = 0
                
        
    else:
        # A의 조합 선택
        for i in range(start, N):
            C[idx_list[i]] = 1
            # 그냥 조합: 다음 인덱스, 다음 숫자
            combination(idx+1, i+1)
            C[idx_list[i]] = 0
        


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    food_list = [list(map(int, input().split())) for _ in range(N)]
    
    # 인덱스 리스트 생성
    idx_list = [hi for hi in range(N)]
    C = [0]*N
    R = N//2
    
    # A, B 맛의 합, 시너지 최솟값
    A = 0
    B = 0
    minn = 20000*8
    
    # 조합 적용
    combination(0, 0)
    
    # 결과 출력
    print(f'#{t} {minn}')