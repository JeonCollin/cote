T = int(input())

for t in range(1, T+1):

    # L 칼로리를 넘지 않아야 함
    N, L = list(map(int, input().split()))

    # 맛, 칼로리
    mylist = [0]*N

    for n in range(N):
        mylist[n] = list(map(int, input().split()))

    # 최대 맛
    maxT = 0

    # 비트마스킹을 이용한 부분집합 선정
    # 전체 부분집합의 개수 만큼 루프를 돌린다
    for i in range(1 << N):
        # 특정한 모습의 i가 나온다
        # i == 10101 이라고 가정

        # 부분집합의 맛, 칼로리 초기화
        taste = 0
        calo = 0

        for j in range(N):

            # j를 shifting 한 부분이 1이라면
            # 즉 0,2,4번째 인덱스
            if(i & (1 << j)):
                taste += mylist[j][0]
                calo += mylist[j][1]

        # 최대 값 갱신: 칼로리가 어느 정도 이하일 때
        if(taste >= maxT and calo <= L):
            maxT = taste

    print(f'#{t} {maxT}')