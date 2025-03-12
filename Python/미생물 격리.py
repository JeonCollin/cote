import copy

#객체 이동
def move(obj):
    #상
    if(obj[3] == 1):
        obj[0] -= 1

    #하
    elif(obj[3] == 2):
        obj[0] += 1

    #좌
    elif(obj[3] == 3):
        obj[1] -= 1

    #우
    elif(obj[3] == 4):
        obj[1] += 1

#경계에 걸릴 경우
def half_change(obj):

    #경계에 있다면
    if(obj[0] == 0 or obj[0] == N-1 or obj[1] == 0 or obj[1] == N-1):
        #미생물 수는 반으로 줄어든다
        obj[2] = obj[2]//2

        #방향은 반대로 바뀐다
        #상
        if(obj[3] == 1):
            obj[3] =  2

        #하
        elif(obj[3] == 2):
            obj[3] = 1

        #좌
        elif(obj[3] == 3):
            obj[3] = 4

        #우
        elif(obj[3] == 4):
            obj[3] = 3

#병합
def merge(group):
    # 미생물1 ~ 미생물K 까지 살펴본다
    # 같은 좌표인 미생물이 있다면 합친다
    i = 0
    
    while True:
        # 각종 파라미터 초기화
        temp_list = []
        temp_idx = 0
        L = len(group)
        # 종료조건: idx out of range
        if(i >= L):
            break
        # 스킵: [0,0,0,0]
        if(group[i] == [0,0,0,0]):
            i += 1
            continue
        row = group[i][0]
        col = group[i][1]
        
        # 그룹에서 같은 좌표의 미생물을 찾자
        for j in range(i, L):
            # 같은 좌표인 미생물이 있다면 확인리스트에 추가한다
            if(group[j][0] == row and group[j][1] == col):
                temp_list.append(copy.deepcopy(group[j]))
                # dummy data 입력
                group[j] = [0,0,0,0]
                temp_idx = j
                
        # 해당 칸에 미생물 그룹이 2개 이상인 경우는 합병
        # 해당 칸에 미생물 그룹이 2개 이상인 경우에만 합병
        if(len(temp_list) >= 2):
        # 해당 칸의 미생물 중 최고를 고른다
            maxx = 0
            sumn = 0
            idx = 0
            for j in range(len(temp_list)):
                # 미생물 수 합치기
                sumn += temp_list[j][2]
                    
                # 최대 값 갱신, 인덱스 기록
                if(maxx < temp_list[j][2]):
                    maxx = temp_list[j][2]
                    idx = j
                
            # 방향: 최대 미생물의 방향
            direction = temp_list[idx][3]
                
            # 합친 결과를 그룹에 넣는다
            group[temp_idx] = copy.deepcopy([row, col, sumn, direction])
                
        elif(len(temp_list) == 1):
            group[temp_idx] = copy.deepcopy(temp_list[0])
        
        i += 1        


T = int(input())

for t in range(1, T+1):

    #N:셀의 크기, M:시간, K:군집의 수
    N, M, K = list(map(int, input().split()))

    #군집 정보 받기(row,col,미생물수,이동방향)
    #1상 2하 3좌 4우
    group = [list(map(int, input().split())) for _ in range(K)]

    #알고리즘
    #움직임, 반감, 합쳐짐
    #주어진 시간동안 움직인다
    for _ in range(M):

        #모든 군집들을 살펴본다
        for obj in group:
            
            #이동
            move(obj)

            #반감
            half_change(obj)

        #합병
        merge(group)
        #print(group)
        
    #남아있는 미생물 수 계산
    sum = 0
    
    for obj in group:
        sum += obj[2]
    
    #결과 출력
    print(f'#{t} {sum}')