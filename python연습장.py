def push(item):

    # 일단 top 증가
    global top
    top += 1

    # overflow
    if(top == len(stack)):
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


def is_arrive(adj_arr, S, G):

    # 방문기록
    visited = [0] *51

    start = S
    end = G

    visited[start] = 1 

    while True:
       
       # 방문기록
        if(visited[start] == 0):
            visited[start] = 1 

        for node in range(len(adj_arr[start])):
            # 이어져 있고 방문한 적이 없다면 방문한다
            if(adj_arr[start][node] == 1 and visited[node] == 0):
                # 방문 기록
                # visited[node] = 1
                # print('A',start)
                # 이전 위치는 stack에 저장
                push(start)
                # 노드 변경
                start = node

                # 종료조건: 도착점일 경우
                if(start == end):
                    return 1
                
                break
                
        # 물러나는 경우: 연결된 곳이 없을 때
        # 또는 이미 방문한 곳일 때
        else:
            # print('b', start)
            start = pop()
            # print('c', start)

            # 종료조건: 도착하지 못한 경우
            # 시작보다 더 뒤로 가게된다
            if(start == False):
                return 0

T = int(input())

for t in range(1, T+1):

    # V개의 노드와 E개의 간선
    V, E = list(map(int, input().split()))

    # 스택 초기화
    top = -1
    stack = [0]*(V+1) # 노드가 1번부터 시작함

    # 노드 최대 수가 50개 이므로 
    # 2차원 행렬을 사용하는 것이 더 좋아보인다
    # 숫자가 1부터 시작해서 51개로 만들어야 함
    adj_arr = [[0]*51 for _ in range(51)]

    # E번 동안 출발, 도착 노드 정보가 주어짐
    for e in range(E):
        start, arrive = list(map(int, input().split()))
        adj_arr[start][arrive] = 1

    # 마지막에 진짜 출발점과 도착노드가 주어짐
    S, G = list(map(int, input().split()))

    # 결과출력
    print(f'#{t} {is_arrive(adj_arr, S, G)}')