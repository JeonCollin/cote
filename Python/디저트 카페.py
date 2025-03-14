'''
- N x N 행렬에서
갯수: a = 우하 = 좌상
갯수: b = 좌하 = 우상
a + b <= N-1
단 a, b 둘 다 1 이상

- 움직일 때는
a + b == 2 >> 3x3칸을 움직임 >> 인덱스: 1 ~ N-2
a + b == 3 ?? 4x4칸을 움직임 >> 인덱스: 1 ~ N-2
결론: 유효인덱스 == 1 ~ N-2
'''

# 방향벡터: 시계방향으로
# (우하) [좌하] (좌상) [우상]
drow = [1,  1, -1, -1]
dcol = [1, -1, -1,  1]

def move_cafe(a, b):
    global N
    global maxx
    
    # 디저트 기록 리스트
    dessert = [0]*(a+b)*2
    
    # 실제 적용할 방향벡터
    dr = [drow[0]]*a + [drow[1]]*b + [drow[2]]*a + [drow[3]]*b
    dc = [dcol[0]]*a + [dcol[1]]*b + [dcol[2]]*a + [dcol[3]]*b
    
    # 유효 인덱스 내에서 움직인다
    for row in range(0, N):
        for col in range(0, N):
            
            # 파라미터 초기화
            dessert = []
            ROW = row
            COL = col
            
            # 방향벡터로 움직인다
            for i in range(2*(a+b)):
                ROW += dr[i]
                COL += dc[i]
                # 범위를 벗어나지 않게 조정
                if(0 <= ROW < N and 0 <= COL < N):
                    # 디저트를 추가
                    dessert.append(dessert_cafe[ROW][COL])
                    
            #print(dessert)
            # 정상적으로 돌았다면 길이가 2(a+b)임
            if(len(dessert) == 2*(a+b)):
                
                # 겹치는 디저트가 있으면 안된다
                for j in range(len(dessert)-1):
                    for k in range(j+1, len(dessert)):
                        # 같은 디저트가 있다면 무효
                        if(dessert[j] == dessert[k]):
                            dessert = []
                            break
            
                # 디저트 최대 길이 갱신
                if(len(dessert) > maxx):
                    maxx = len(dessert)

                    
    

T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    
    dessert_cafe = [list(map(int, input().split())) for _ in range(N)]
    
    # 최대값 초기화
    maxx = 0
    
    # 방향에 대한 조합 생성    
    for a in range(1, N-1):
        for b in range(1, N-1):
            
            # 둘의 합이 N-1 이하면 유효
            if(a + b <= N-1):
                
                # 특정 a,b 조합이 선택됨.
                # 좌표에서 실제로 이동시켜보자
                move_cafe(a,b)
    
    # 만약 먹을 수 없는 경우는 -1 리턴
    if(maxx == 0):
        maxx = -1
    
    # 결과출력
    print(f'#{t} {maxx}')