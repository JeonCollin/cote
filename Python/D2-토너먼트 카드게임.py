def who_win(A, B):
    # 이긴사람의 인덱스, 낸 것
    if([A,B] == [1,1]):
        return [A,1]
    
    elif([A,B] == [1,2]):
        return [B,2]
    
    elif([A,B] == [1,3]):
        return [A,1]
    
    elif([A,B] == [2,1]):
        return [A,2]
    
    elif([A,B] == [2,2]):
        return [A,2]
    
    elif([A,B] == [2,3]):
        return [B,3]
    
    elif([A,B] == [3,1]):
        return [B,1]
    
    elif([A,B] == [3,2]):
        return [A,3]
    
    elif([A,B] == [3,3]):
        return [A,3]
    

def tournament(arr, start, end):

    middle = (start + end) // 2
    
    # 종료조건1: 길이가 1
    if(start == middle or end == middle+1):
        return arr[middle]
    
    # 종료조건2: 길이가 2
    elif(middle-start == 1):
        return who_win(start, middle)
    
    elif(end-(middle+1) == 1):
        return who_win(middle+1, end)

    else:
        # 중간지점 좌측
        tournament(arr, start, middle)
        # 중간지점 우측
        tournament(arr, middle+1, end)
        

    

T = int(input())

for t in range(1, T+1):

    # N: 인원 수
    N = int(input())

    # N명이 고른 카드 번호
    # 1가위 2바위 3보
    cards = list(map(int, input().split()))

    # N명을 토너먼트로 나누자
    start = 0
    end = N-1
    result = tournament(cards, start, end)

    # 결과출력
    print(f'#{t} {result[0]}')