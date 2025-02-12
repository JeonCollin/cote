def main(group, M):

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

    #남아있는 미생물 수 계산
    sum = 0
    for obj in group:
        sum += obj[2]

    return sum

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
    else:
        obj[0] += 1

#경계에 걸릴 경우
def half_change(obj):

    #경계에 있다면
    if(obj[0] == 0 or obj[0] == 6 or obj[1] == 0 or obj[1] == 6):
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
        if(obj[3] == 3):
            obj[3] = 4

        #우
        if(obj[3] == 4):
            obj[3] = 3

#병합
def merge(group):
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

    #N:셀의 크기, M:시간, K:군집의 수
    N, M, K = list(map(int, input().split()))

    #군집 정보 받기(row,col,미생물수,이동방향)
    #1상 2하 3좌 4우
    group = [list(map(int, input().split())) for _ in range(K)]

    #알고리즘
    #결과 출력
    print(f'#{t} {main(group, M)}')