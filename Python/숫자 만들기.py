def permutation(data, r, result = []):

    #중복순열 생성 완료
    if len(result) == r:
        return result
    
    for i in range(len(data)):
        permutation(data, r, result + data[i])

T = int(input())

for t in range(1, T+1):

    N = int(input())

    #연산자 종류과 개수 받기
    operands = list(map(int, input().split()))

    #수식에 사용될 숫자 받기
    numbers = list(map(int, input().split()))

    #연산자의 순열                 
    print(permutation(operands, N-1))


    #결과 출력
    #print(f'#{t} {}')