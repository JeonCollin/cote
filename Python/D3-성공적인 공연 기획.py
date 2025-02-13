def crowd(mylist):

    L = len(mylist)
    # 박수치는데 모자란 인원 수
    rest = 0
    # 모자란 인원 수 누적
    sum_rest = 0

    # 지금 박수치고 있는 사람 수
    # 첫 번째 사람들은 무조건 다 박수침
    all = people[0]

    # i명이 박수를 쳐야
    # people[i]에 있는 사람들이 박수를 친다: people[i] == 명 수

    #길이가 1이라면 무조건 박수 친다
    if(L == 1):
        return 0
    
    for i in range(1, L):
            
        # 박수치는 인원이 모자라지 않을 경우
        if(all >= i):
            all += people[i]

        # 박수치는 인원이 모자란 경우
        # 얼만큼 모자른지 차이를 구하고 박수치게 만든다
        else:
            # 지금 단계에서 모자란 인원 수
            rest =  i - all
            sum_rest += rest

            # 그 인원 수 만큼 더해주자
            # 그리고 박수 쳤다고 가정해 주자
            all = all + rest + people[i]

    return sum_rest


T = int(input())

for t in range(1, T+1):

    # 사람: 첫 번째 문자열은 현재 박수 중인 사람 
    # 그 뒤로는 박수 칠 사람 수
    # i번째 글자는 기립박수 하는 사람이 i-1명 이상일 때
    # 박수를 치는 사람임
    people = list(map(int, input()))

    # 결과출력
    print(f'#{t} {crowd(people)}')