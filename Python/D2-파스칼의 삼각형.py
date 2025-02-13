def pascal(N):
    #파스칼의 삼각형
    arr = [1]*N

    #초기값 설정: 초기값은 더해나갈 수가 없다
    if(N == 1):
        return [1]
    
    elif(N == 2):
        return [1, 1]
    
    #그 외: 그 전 파스칼의 양 옆 합
    else:
        for idx in range(1, N-1):
            arr[idx] = pascal(N-1)[idx-1] + pascal(N-1)[idx]

        return arr

T = int(input())

for t in range(1, T+1):

    #N줄
    N = int(input())

    #결과 출력
    print(f'#{t}')
    for i in range(1, N+1):
        result = ' '.join(map(str, pascal(i)))
        print(result)