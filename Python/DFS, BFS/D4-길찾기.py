def stack_init():
    global stack
    global top

    stack = [0]*100
    top = -1

def push(item):

    global top

    # 일단 top 증가
    top += 1

    # overflow
    if(top == 100):
        print('overflow')

    # 아니면 push
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
    

def DFS(adj):

    # 방문리스트를 생성한다(0~99)까지 있음
    visited_list = [0]*100

    # 시작점 = 0, 끝점 = 99
    node = 0
    end = 99

    # 알고리즘
    while True:
        
        if(adj[node] != [] and adj[node] == 0):
            #visited_list[node] = 1
            pass

        # 현재 있는 노드에서 갈 수 있는 경로를 방문한다
        for idx in range(0, len(adj[node])):
            # 방문한 적이 없는 곳이라면 갈 수 있다.
            # 현재 장소를 push하고 나서 방문한다
            # 가고 나서 방문 등록을 해준다
            # print(idx)
            if(visited_list[adj[node][idx]] == 0):
                push(node)
                node = adj[node][idx]
                visited_list[node] = 1
                # print('b', node)
                # 그곳이 끝 점이라면 끝난다
                if(node == end):
                    return 1
                
                break

        # 더 이상 갈 수 있는 곳이 없다면 pop하여 돌아간다
        # 갈 수 없는곳 = 끝 부분
        else:
            node = pop()
            # print('c', node)
            # 돌고돌아 태초마을이라면 실패
            if(node == False):
                return 0

            

            

stack = [0]*100
top = -1

for t in range(1, 11):

    # 스택 초기화
    stack_init()

    # N = 길의 개수
    T, N = list(map(int, input().split()))

    # 정점의 최대 개수는 100개이다. 갈림길도 최대 2개이다
    # 인접리스트로 푸는 것이 좋아보인다.
    adj = [[] for _ in range(100)]

    # 길이 연결된 순서쌍: 0출발 99도착
    inputlist = list(map(int, input().split()))

    # 인접리스트 생성
    for i in range(0, len(inputlist), 2):

        adj[inputlist[i]].append(inputlist[i+1])

    # for i in range(100):
    #     print(adj[i])

    # 결과 출력
    print(f'#{t} {DFS(adj)}')