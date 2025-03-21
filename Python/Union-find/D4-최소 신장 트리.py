'''
Prim, Kruckal 문제인데
간선수가 100만개임
간선 수가 많을 수록 크루스칼이 불리함
그래서 Prim으로 풀면 ㄱㅊ은데
Kruskal로 풀면 터진다
'''

################ 최소힙 ###############################
def enqueue(item):
    global root
    global rear
    
    rear += 1
    heap[rear] = item

    c = rear
    p = c//2
    
    while(p >= root):
        if(heap[p][1] >= heap[c][1]):
            heap[p], heap[c] = heap[c], heap[p]
            
        c = p
        p = c//2
        
def dequeue():
    global root
    global rear
    
    temp = heap[root]
    heap[root] = heap[rear]
    heap[rear] = 0
    rear -= 1
    
    p = root
    c = 2*p
    
    while(c <= rear):
        if(c+1 <= rear and heap[c+1][1] <= heap[c][1]):
            c += 1
            
        if(heap[p][1] >= heap[c][1]):
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = 2*p
            
        else:
            break
        
    return temp

#########################################################

def partition(left, right):
    global mylist
    
    # 가장 왼쪽을 피봇으로 삼는다
    pivot = mylist[left][2]
    i = left
    j = right
    
    # cross 전까지
    while(i < j):
        # 왼쪽에서 pivot보다 큰 원소 찾기
        while(i <= right and pivot >= mylist[i][2]):
            i += 1
        # i 찾음
        
        # 오른쪽에서 pivot보다 작은 원소 찾기
        while(j >= left and pivot < mylist[j][2]):
            j -= 1
        # j 찾음
        
        # cross가 아니면 둘이 바꾼다
        if(i < j):
            mylist[i], mylist[j] = mylist[j], mylist[i]
            
    # 처음과 피봇을 바꾼다
    mylist[left], mylist[j] = mylist[j], mylist[left]
    
    # 피봇인덱스 반환
    return j


def quick_sort(left, right):
    
    # 2개 이상의 리스트면 정렬
    if(left < right):
        pivot_idx = partition(left, right)
        # 피봇 인덱스 기준으로 정렬
        quick_sort(left, pivot_idx-1)
        quick_sort(pivot_idx+1, right)

################################################################

def find(a):
    global parents
    # 본인이 부모
    if(parents[a] == a):
        return a
    
    # comrehension
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    # 대표자 찾기
    ap = find(a)
    bp = find(b)
    
    # 둘 중 더 작은 아이가 대표
    if(ap < bp):
        parents[bp] = ap
    else:
        parents[ap] = bp
    

################################################################

def Prim(start):
    global adj_arr
    
    # 방문 기록
    used = [0]*(V+1)
    move = 0
    distance = 0
    
    # 시작점 기록
    # 현재위치, 다음 가중치, 누적거리, 이동 횟수
    enqueue([start, 0, 0])
    
    '''
    BFS는 어차피 최소 가중치만 골라서 간다
    그래서 deq로 받을 때 마다 갱신하면 된다
    '''
    while True:
        
        # 위치 받기
        node = dequeue()
        # 만약 가중치가 커서 이제야 방문한 것이라면 스킵
        if(used[node[0]] == 1):
            continue
        
        # 방문기록, 이동횟수, 누적 가중치 기록
        used[node[0]] = 1
        move += 1
        distance += node[1]
 
        # 만약 모든 곳을 순회 했으면 결과 리턴
        if(move == V+1):
            return distance
        
        # 인접한 곳 찾기
        for i in range(V+1):
            # 0이 아니고, 사용한 적 없다면 갈 수 있다
            if(adj_arr[node[0]][i] != 0 and used[i] == 0):
                # 해당 위치 정보 저장
                enqueue([i, adj_arr[node[0]][i]])

#################################################################

def Kruskal():
    global E
    global mylist
    # 가중치의 크기에 따라 정렬한다
    quick_sort(0, E-1)
    
    distance = 0
    cnt = 0

    # 간선의 정보를 바탕으로 순서대로 union한다
    for i in range(E):        
        # 대표가 다를 때만 합칠 수 있다
        if(find(mylist[i][0]) != find(mylist[i][1])):
            union(mylist[i][0], mylist[i][1])
            # 합치고 가중치와 방문 수 갱신
            distance += mylist[i][2]
            cnt += 1

        # 모든 정점을 돌았으면 끝낸다
        if(cnt == V):
            return distance

################################################################

T = int(input())

for t in range(1, T+1):
    
    # 0 ~ V 노드번호, 간선 수 E
    V, E = list(map(int, input().split()))
    
    # 인접행렬 생성
    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    
    # node1, node2, 가중치 리스트 생성
    mylist = []
    # 부모 리스트 생성
    parents = [hi for hi in range(V+1)]
    
    for e in range(E):
        # 그래프로 만든다: 양방향
        # 노드1, 노드2, 가중치
        n1, n2, w = list(map(int, input().split()))
        adj_arr[n1][n2] = w
        adj_arr[n2][n1] = w
        
        mylist.append([n1, n2, w])
    
    # 힙 초기화
    heap = [0]*(V+1)*(V+1)
    root = 1
    rear = 0
    
    # P = Prim(0)
    K = Kruskal()
    
    # 결과 출력
    print(f'#{t} {K}')