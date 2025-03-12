def swap_card(time):
    global max_num
    global origin_cards
    global cards
    global temp_max
    global possible_max
    
    
    
    # 재귀구조 + 순열
    if(time == N):
        # 바꾼 카드 완성
        # 숫자열로 바꾸기
        temp = ''
        for j in range(len(cards)):
            temp += cards[j]
        
        num = int(temp)
        # print(num)
        # 최대값 갱신
        if(num > max_num):
            max_num = num
        return

    else:
        # 바꿀 카드를 선정
        for i in range(len(cards)-1):
            for j in range(i+1, len(cards)):
                # 바꾼다
                cards[i], cards[j] = cards[j], cards[i]              
                swap_card(time+1)
                # 카드를 원래대로 돌려놓는다
                cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for t in range(1, T+1):
    
    mylist = list(input().split())
    
    # 숫자카드, 교환횟수
    cards = list(mylist[0])
    origin_cards = cards[:]
    N = int(mylist[1])
    
    # 가능한 최대 값
    temp_max = sorted(origin_cards, reverse=True)
    possible_max = ''
    for i in range(len(temp_max)):
        possible_max += temp_max[i]
        
    possible_max = int(possible_max)
    
    max_num = 0
    
    swap_card(0)
    
    # 결과 출력
    print(f'#{t} {max_num}')
    