def find(a):
    global parents
    
    # 자기 자신이면 본인이 조장 리턴
    if(parents[a] == a):
        return a
    
    # 본인이 조장이 아니면 그 위 조장을 찾는다
    return find(parents[a])

def union(a, b):
    # a와 b의 조장을 찾는다
    aRoot = find(a)
    bRoot = find(b)
    
    # 한 대표자를 다른 대표자의 자식으로 만든다
    # 규칙: 번호가 작은 아이 우선
    if(aRoot < bRoot):
        parents[bRoot] = aRoot
        
    else:
        parents[aRoot] = bRoot

T = int(input())

for t in range(1, T+1):
    
    # 1~N 출석번호, M장의 신청서
    N, M = list(map(int, input().split()))

    # 1. make-set
    #  조장 리스트 만들기
    # 일단은 자기 자신
    parents = [hi for hi in range(N+1)]

    # 부모 기록
    mylist = list(map(int, input().split()))

    # 2. union
    for i in range(0, 2*M, 2):
        # 앞에 있는 애가 조장, 조원
        union(mylist[i], mylist[i+1])

    # 3. find
    # 조장이 총 몇 명인지 센다
    result = [0]*(N+1)
    
    for i in range(1, N+1):
        # i의 조장을 찾는다
        a = find(i)
        # 해당 조장 인덱스를 on
        result[a] = 1

    # print(result)
    cnt = 0
    
    for i in range(N+1):
        if(result[i] != 0):
            cnt += 1

    # 결과 출력
    print(f'#{t} {cnt}')