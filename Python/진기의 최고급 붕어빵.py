def counting_list(arr):

    #인덱스: 방문하는시간: 0 1 2 3 4 5 6 .... 
    # 요소 :   방문손님수: 0 8 2 0 7 4 1 ...

    #0이상 11111이하
    count_list = [0]*11112

    #배열을 순회하며 카운팅 리스트를 만든다
    for i in range(len(arr)):
        count_list[arr[i]] += 1

    return count_list


def sell(M, K, input_list):
    #input_List는 카운팅리스트로 들어올거다
    #M초의 시간을 들여 K개의 붕어빵을 만든다

    #카운팅 리스트를 순회하자
    for i in range(len(input_list)):
        #카운팅리스트에서 가장 최소값인 인덱스 찾기
        if(input_list[i] != 0):
            min = i
            break

    #실패경우1: 첫 손님이 만드는 시간보다 빨리 온다
    if(min < M):
        return 'Impossible'
    
    #실패경우2: 방문손님이 현재 있는 붕어빵보다 많다
    sum = 0
    fish = 0

    #카운팅리스트를 순회하자
    for i in range(min, len(input_list)):
        
        #방문 손님이 없는 경우는 무시
        if(input_list[i] == 0):
            continue

        #i: 손님이 방문하는 시간
        #input_list[i]: 방문하는 손님 수
        #i보다 작은 M의 최대 배수 찾기        

        #만든 붕어빵 수        
        fish = (i//M) * K

        #방문한 손님 수 누적
        sum += input_list[i]

        #실패경우2: 붕어빵 수가 누적 손님보다 적다면 오류
        if(fish < sum):
            return 'Impossible'

    #정상적으로 루프 순회를 마무리했다면 끝
    return 'Possible'
        


T = int(input())

for t in range(1, T+1):

    #N명의 사람: 언제 도착하는지
    #M초의 시간을 들이면
    #K개의 붕어빵을 만듬
    N, M, K = list(map(int, input().split()))

    customer = list(map(int, input().split()))


    print(f'#{t} {sell(M, K, counting_list(customer))}')