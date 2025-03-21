'''
환경 부담금: E x L^2
환경 부담금을 최소로 하며, N개의 모든 섬을 연결

크루스칼로 구현
'''
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
        
########################################################################

def distance(x1, x2, y1, y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)



def find(a):
    
    # 본인이 대표면 리턴
    if(parents[a] == a):
        return a
    
    # 경로 압축
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    
    # a와 b의 부모
    ap = find(a)
    bp = find(b)
    
    # 번호가 더 작은 애가 부모가 된다
    if(ap < bp):
        parents[bp] = ap
        
    else:
        parents[ap] = bp
    
def Kruscal():
    global x_list
    global y_list
    global mylist
    
    cost = 0
    cnt = 0
    
    # 비용이 최소인 순서대로 유니온한다
    for i in range(len(mylist)):
        # 대표자가 다를 때만 유니온
        if(find(mylist[i][0]) == find(mylist[i][1])):
            continue
        
        union(mylist[i][0], mylist[i][1])
        
        # 비용과 합친 횟수 계산
        cnt += 1
        cost += mylist[i][2]
        
        # 총 노드 수 N개 >> 간선 N-1개
        # 간선 수 만큼 합쳤으면 끝
        if(cnt == N-1):
            return cost*E


    
T= int(input())

for t in range(1, T+1):
    
    # 섬의 개수
    N = int(input())
    
    # 0번 ~ N-1번의 섬들
    # 일단은 자기 자신이 부모가 된다
    parents = [hi for hi in range(N)]
    
    # 섬들의 x좌표
    x_list = list(map(int, input().split()))
    
    # 섬들의 y좌표
    y_list = list(map(int, input().split()))
    
    # 환경 부담 세율
    E = float(input())
    
    # n1, n2, 거리 리스트 생성
    mylist = []
    
    for i in range(N-1):
        for j in range(i+1, N):
            x1 = x_list[i]
            x2 = x_list[j]
            
            y1 = y_list[i]
            y2 = y_list[j]
            
            # print("좌표:",x1, x2, y1, y2)
            
            # 거리
            l = distance(x1, x2, y1, y2)
            # print("거리:",l)
            
            # n1, n2, 거리 리스트 생성
            temp = [i, j, l]
            
            mylist.append(temp)
            
    # l을 기준으로 오름차순 정렬
    
    quick_sort(0, len(mylist)-1)
    
    # print(mylist)
    
    min_cost = Kruscal()
    
    # 소수점 첫째 자리에서 반올림
    result = round(min_cost)
    
    # 결과 출력
    print(f'#{t} {result}')
    