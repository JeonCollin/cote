def selectionSort(data, N):

    #데이터를 순회하며 큰작큰작... 순서로 정렬
    for i in range(N):
        #최대 최소 초기화
        min = data[i]
        max = data[i]

        min_i = i
        max_i = i

        #리스트를 순회하며 최대/최소를 찾는다
        for j in range(i, N):
            if(min >= data[j]):
                min = data[j]
                min_i = j
            
            if(max <= data[j]):
                max = data[j]
                max_i = j

        #짝수 번째 인덱스에는 최대값 정렬
        if(i%2 == 0):
            temp = data[max_i]
            data[max_i] = data[i]
            data[i] = temp

        #홀수 번째 인덱스에는 최소값 정렬
        if(i%2 == 1):
            temp = data[min_i]
            data[min_i] = data[i]
            data[i] = temp

    return data

T = int(input())

for t in range(1, T+1):

    N = int(input())

    #사용될 숫자 받기
    numbers = list(map(int, input().split()))

    #선택정렬 사용
    #큰 작 큰 작 ... 순서
    result = selectionSort(numbers, N)

    #결과 출력
    print(f'#{t}', end='')
    for idx in range(10):
        print(f' {result[idx]}', end='')
    print()