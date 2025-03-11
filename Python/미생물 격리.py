def main(coordiante, M):

    #움직임, 반감, 합쳐짐

    #주어진 시간동안
    for _ in range(M):

        # 움직인다
        move()
        # 합병한다
        merge()
        # 반감한다
        half_change()
        
    # 남은 미생물 수 계산
    sum = 0
    for row in range(N):
        for col in range(N):
            if(coordiante[row][col] != 0):
                sum += coordiante[row][col][0]

    return sum

#객체 이동
def move():
    
    # 좌표에 있는 모든 객체 이동
    for row in range(N):
        for col in range(N):
            
            # 객체 선택
            if(coordinate[row][col] != 0):
                
                # 상
                if(coordinate[row][col][1] == 1):
                    # 한 칸 이동
                    coordinate[row-1][col] = coordinate[row][col]
                    # 이동했으면 지운다
                    coordinate[row][col] = 0
                    
                # 하
                elif(coordinate[row][col][1] == 2):
                    # 한 칸 이동
                    coordinate[row+1][col] = coordinate[row][col]
                    # 이동했으면 지운다
                    coordinate[row][col] = 0
                
                # 좌
                elif(coordinate[row][col][1] == 3):
                    # 한 칸 이동
                    coordinate[row][col-1] = coordinate[row][col]
                    # 이동했으면 지운다
                    coordinate[row][col] = 0
                    
                # 우
                elif(coordinate[row][col][1] == 4):
                    # 한 칸 이동
                    coordinate[row][col+1] = coordinate[row][col]
                    # 이동했으면 지운다
                    coordinate[row][col] = 0
                

#경계에 걸릴 경우
def half_change():

    # 좌표에 있는 모든 객체의 경계 확인
    for row in range(N):
        for col in range(N):
            
            # 객체 선택
            if(coordinate[row][col] != 0):
                
                # 경계인지 확인
                if(row == 0 or row == N-1 or col == 0 or col == N-1):
                    # 상
                    if(coordinate[row][col][1] == 1):
                        # 상 >> 하
                        coordinate[row][col][1] = 2
                        # 반감
                        coordinate[row][col][0] //= 2
                        
                    # 하
                    elif(coordinate[row][col][1] == 2):
                        # 하 >> 상
                        coordinate[row][col][1] = 1
                        # 반감
                        coordinate[row][col][0] //= 2
                    
                    # 좌
                    elif(coordinate[row][col][1] == 3):
                        # 좌 >> 우
                        coordinate[row][col][1] = 4
                        # 반감
                        coordinate[row][col][0] //= 2
                        
                    # 우
                    elif(coordinate[row][col][1] == 4):
                        # 우 >> 좌
                        coordinate[row][col][1] = 3
                        # 반감
                        coordinate[row][col][0] //= 2


#병합
def merge():
    for i in range(1, len(group)):
        for j in range(i):

            #좌표가 똑같다면
            if(group[i][0] == group[j][0] and group[i][1] == group[j][1]):

                #더 많은 쪽으로 합병된다
                if(group[i][2] > group[j][2]):
                    group[i][2] += group[j][2]
                    group[j] = [0, 0, 0, 0]

                else:
                    group[j][2] += group[i][2]
                    group[i] = [0, 0, 0, 0]


T = int(input())

for t in range(1, T+1):

    # N:셀의 크기, M:시간, K:군집의 수
    N, M, K = list(map(int, input().split()))

    # 군집 정보 받기(row,col,미생물수,이동방향)
    # 1상 2하 3좌 4우
    group = [list(map(int, input().split())) for _ in range(K)]
    
    # 좌표에 미생물을 적는게 편할듯
    coordinate = [[0]*N for _ in range(N)]
    
    # 미생물을 좌표에 집어넣자
    # 수, 방향만!
    for i in range(K):
        coordinate[group[i][0]][group[i][1]] = [group[i][2], group[i][3]]

    # 알고리즘
    # 결과 출력
    print(f'#{t} {main(coordinate, M)}')