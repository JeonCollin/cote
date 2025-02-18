def who_win(A, B):
    global cards
    # 이긴사람의 인덱스, 낸 것
    if([cards[A],cards[B]] == [1,1]):
        return A
    
    elif([cards[A],cards[B]] == [1,2]):
        return B
    
    elif([cards[A],cards[B]] == [1,3]):
        return A
    
    elif([cards[A],cards[B]] == [2,1]):
        return A
    
    elif([cards[A],cards[B]] == [2,2]):
        return A
    
    elif([cards[A],cards[B]] == [2,3]):
        return B
    
    elif([cards[A],cards[B]] == [3,1]):
        return B
    
    elif([cards[A],cards[B]] == [3,2]):
        return A
    
    elif([cards[A],cards[B]] == [3,3]):
        return A
    

def tournament(arr, start, end):
    # arr의 인덱스가 사람이고
    # arr의 내용물이 가위바위보
    middle = (start + end) // 2
    
    # 종료조건1: 길이가 1
    if(start == end):
        return start

    else:
        # 중간지점 좌측
        winner_left = tournament(arr, start, middle)

        # 중간지점 우측
        winner_right = tournament(arr, middle+1, end)

        return who_win(winner_left, winner_right)
        
'''
재귀함수는... 수열처럼 생각하자
초기 조건 주고나서
일반항을 이끌어내면 된다
'''
    

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
    # 사람은 1부터고 인덱스는 0부터임
    result = tournament(cards, start, end) + 1

    # 결과출력
    print(f'#{t} {result}')
