def push(item):
    global V
    global top
    # 일단 top 증가
    top += 1

    # overflow
    if(top == V):
        print('overflow')

    # push
    else:
        stack[top] = item

def pop():
    global top

    # underflow
    if(top == -1):
        return False

    # pop
    else:
        top -= 1
        return stack[top+1]
    
def DFS(addj_arr, S, G, V):

    # 방문한 노드는 기록해놓는다
    # 일단 초기화
    visited = [0]*(V+1)

    L = len(addj_arr)
    start = S

    # S에서 G로 갈 수 있는지 확인해보자
    while True:

        # 지금 있는 노드를 방문했다고 기록한다
        if(visited[start] == 0):
            visited[start] = 1
        #     # print('ㄱ',start)
        #     # print(visited[start])
            

        # 지금 있는 노드에서 갈 수 있는 곳을 확인한다
        for node in range(1, L):
            # 갈 수 있는 곳이고, 방문한 적 없다면
            if(addj_arr[start][node] == 1 and visited[node] == 0):
                visited[node] = 1
                # 스택에 저장
                push(start)
                # 노드 이동
                start = node
                print('ㄴ',start)
                # print(visited[start])

                #간 곳이 도착점이라면 게임 종료
                if(start == G):
                    return 1

        # 이미 방문한 노드면 돌아간다
        else:
            start = pop()
            print('ㄷ',start)
            # print(visited[start])
            # underflow 상황이면 G에 도착 못하는 거임
            if(start == False):
                return 0




T = int(input())

for t in range(1, T+1):

    # V개의 노드, E개의 간선: 간선이 연결된 정보임
    V, E = list(map(int, input().split()))

    # 간선 정보 리스트 생성: 인접행렬 초기화
    adj_arr = [[0]*(V+1) for _ in range(V+1)]

    # stack 초기화
    stack = [0]*V
    top = -1

    # E개 줄에 걸쳐 출발, 도착 노드로 간선 정보가 주어짐
    # 인접행렬 생성
    for e in range(E):
        v1, v2 = list(map(int, input().split()))
        adj_arr[v1][v2] = 1

    # # 검증용
    # for i in range(V+1):
    #     print(adj_arr[i])
    
    # S: 출발노드, G: 도착노드
    S, G = list(map(int, input().split()))

    # 결과 출력
    print(f'#{t} {DFS(adj_arr, S, G, V)}')