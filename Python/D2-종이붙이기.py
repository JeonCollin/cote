def paper(N):

    #일단 수를 조정하자
    n = N//10

    #저장할 배열 생성
    mypaper = [0]*(n+1)

    #초기값 설정
    mypaper[1] = 1
    mypaper[2] = 3

    #점화식: 붙일 수 있는 종이 = 그 전에 붙인 종이 + 그 전전에 붙인 종이 * 2가지 경우
    for i in range(3,n+1):
        mypaper[i] = mypaper[i-1] + mypaper[i-2]*2

    return mypaper[n]
        


T = int(input())

for t in range(1, T+1):

    N = int(input())

    # 결과 출력
    print(f'#{t} {paper(N)}')