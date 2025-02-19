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


def is_arrive(adj_arr, start, G):
    global answer
    #print(start)
    
    # 방문기록
    visited[start] = 1

    # 인접리스트를 순회하며 갈 수 있는 곳을 찾자
    for node in range(1, len(adj_arr[start])):
        # 이어져 있고 방문한 적이 없다면 방문한다
        if(adj_arr[start][node] == 1 and visited[node] == 0):
            # 종료조건: 도착점일 경우
            #print(node)
            if(node == G):
                # 리턴을 쓰면 현재 함수에 대해서 리턴이라
                # 재귀 구조면 씨알도 안먹힌다
                answer = 1
            # 지금 지점을 node로 이동하고 재귀호출
            # 재귀함수가 컴퓨터 메모리의 stack을 이용하니까
            # 따로 push나 pop을 해줄 필요가 없다
            is_arrive(adj_arr, node, G)


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

    # 방문리스트 생성
    visited = [0] *51

    # E번 동안 출발, 도착 노드 정보가 주어짐
    for e in range(E):
        start, arrive = list(map(int, input().split()))
        adj_arr[start][arrive] = 1

    # 마지막에 진짜 출발점과 도착노드가 주어짐
    S, G = list(map(int, input().split()))

    answer = 0
    is_arrive(adj_arr, S, G)

    # 결과출력
    print(f'#{t} {answer}')