def num_bus(bus, N, bus_stop, P):
    #N:버스노선 갯수
    #P개의 버스 정류장

    num_of_bus = [0]*P

    #버스를 고정하고
    for i in range(N):

        #정류장을 순회하며
        for j in range(P):

            #A이상 B 이하를 찾아내자
            if(bus[i][0] <= bus_stop[j] <= bus[i][1]):

                #머무르는 경우 지나치는 버스 횟수 증가
                num_of_bus[j] += 1

    return num_of_bus

T = int(input())

for t in range(1, T+1):

    #N:버스노선 갯수
    N = int(input())

    #[A이상, B이하]인 정류장만 다니는 버스
    bus = [list(map(int, input().split())) for _ in range(N)]

    #P개의 버스 정류장
    P = int(input())

    #C번 버스 정류장
    C = [0]*P
    for p in range(P):
        C[p] = int(input())

    #[0, 1, 1, 2, ...] 총 p개
    result = num_bus(bus, N, C, P)

    #결과출력
    print(f'#{t}', end=' ')
    for i in range(P-1):
        print(f'{result[i]}', end=' ')

    print(f'{result[P-1]}')