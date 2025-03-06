def in_order(n):
    global result
    # 중위 순회로 글자를 읽는다
    if(n != 0):
        # 좌
        in_order(left[n])
        # 현재
        result += word[n]
        # 우
        in_order(right[n])

for t in range(1, 11):

    # 정점의 수
    N = int(input())

    word = [0]*(N+1)

    # 부모를 인덱스로 삼자
    # 좌 우 아이 받기
    left = [0]*(N+1)
    right = [0]*(N+1)

    # 연결 정보 받기
    for n in range(1, N+1):
        # 일단 입력을 쪼개자
        # 필요한 건 노드와 간선의 정보임
        mylist = list(input().split())

        word[n] = mylist[1]
        
        L = len(mylist)

        # 좌 우 정보를 다 줬다면
        # 둘 다 기록
        if(L == 4):
            left[n] = int(mylist[2])
            right[n] = int(mylist[3])

        # 좌쪽 정보만 줬다면
        # 그것만 기록
        elif(L == 3):
            left[n] = int(mylist[2])

    result = ''
    in_order(1)

    # 결과 출력
    print(f'#{t} {result}')