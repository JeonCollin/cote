def counting_sort(mylist):
    
    # 1단계: 카운팅 배열 생성
    cnt_list = [0]*101
    
    for i in range(len(mylist)):
        cnt_list[mylist[i]] += 1
        
    # 2단계: 유효한 인덱스 누적 합
    sumn = 0
    for j in range(101):
        
        # 유효하지 않은 부분 넘기기
        if(cnt_list[j] == 0):
            continue
        
        # 누적합으로 교체
        sumn += cnt_list[j]
        cnt_list[j] = sumn
        
    # 3단계: cnt를 인덱스로 삼아 정렬
    result = [0]*len(mylist)
    for i in range(len(mylist)):
        cnt_list[mylist[i]] -= 1
        result[cnt_list[mylist[i]]] = mylist[i]
        
    return result

def delivery():
    global weights
    global trucks
    
    # 보낸 화물 무게 합
    spent = 0
    
    # 최소트럭부터 가능한 가장 큰 짐을 옮긴다
    # 트럭은 앞에서 부터, 짐은 뒤에서 부터 보면 편하다
    for t in range(M):
        for w in range(N-1, -1, -1):
            
            # 이미 보낸 화물은 넘긴다
            if(weights[w] == 0):
                continue
            
            # 보낼 수 있는 화물이면 1개만 옮기고 기록
            if(weights[w] <= trucks[t]):
                spent += weights[w]
                weights[w] = 0
                break
                
    return spent
                
T = int(input())

for t in range(1, T+1):
    
    # N 컨테이너 수, M 트럭 수
    N, M = list(map(int, input().split()))
    
    # 화물의 무게
    weights = list(map(int, input().split()))
    
    # 트적의 적재 용량
    trucks = list(map(int, input().split()))
    
    # 트럭 당 한 개의 컨테이너를 운반할 수 있다.
    # 화물을 싣지 못할 수도 있고, 남는 화물이 있을 수도 있다.
    
    # 우선 화물의 무게와 트럭의 적재용량 정렬
    weights = counting_sort(weights)
    trucks = counting_sort(trucks)

    # 결과 출력
    print(f'#{t} {delivery()}')