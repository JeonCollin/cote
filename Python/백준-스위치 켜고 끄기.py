def boy(student, switch_list):
    #student: 성별1, 번호
    N = len(switch_list)

    #남학생은 배수들의 상태를 바꾼다
    for idx in range(student[1]-1, N, student[1]):
        switch_list[idx] = int(not switch_list[idx])

    return switch_list

def girl(student, switch_list):
    #student: 성별2, 번호
    N = len(switch_list)
    col = student[1] - 1
    i = 0
    #여학생들은 번호 기준으로 좌우대칭인 곳까지 바꾼다
    #일단 자기 자신 먼저 켜고 끈다
    switch_list[ col ] = int(not switch_list[ col ])
    
    #인덱스를 벗어나지 않게 한다
    while(col-i >= 0 and col+i < N and switch_list[col-i] == switch_list[col+i]):
        switch_list[col-i] = int(not switch_list[col-i])
        switch_list[col+i] = int(not switch_list[col+i])

        i += 1

    return switch_list

def print_result(final):

    L = len(final)

    for i in range(L-1):
        print(final[i], end=' ')
    print(final[L-1])



num_of_switch = int(input())

switches = list(map(int, input().split()))

num_of_student = int(input())

#학생의 성별(1남자 2여자), 학생이 받은 수
#남자는 번호의 배수들의 상태를 바꾼다
#여학생은 번호 기준으로 좌우대칭인 곳 까지 상태를 바꾼다. 본인 1개도 좌우대칭이다
student_list = [list(map(int, input().split())) for _ in range(num_of_student)]

for student in student_list:
    
    #남학생인 경우
    if(student[0] == 1):
        switches = boy(student, switches)

    #여학생인 경우
    else:
        switches = girl(student, switches)

#결과출력
#20개 이하면 한 줄에 출력
if(num_of_switch <= 20):
    print_result(switches)

#20개 이상이면 나눠서 출력
if(20 < num_of_switch <= 40):
    print_result(switches[ 0:20])
    print_result(switches[20:40])

#40개 이상이면 나눠서 출력
if(40 < num_of_switch <= 60):
    print_result(switches[ 0:20])
    print_result(switches[20:40])
    print_result(switches[40:60])

#60개 이상이면 나눠서 출력
if(60 < num_of_switch <= 80):
    print_result(switches[ 0:20])
    print_result(switches[20:40])
    print_result(switches[40:60])
    print_result(switches[60:80])

#80개 이상이면 나눠서 출력
if(80 < num_of_switch <= 100):
    print_result(switches[ 0:20])
    print_result(switches[20:40])
    print_result(switches[40:60])
    print_result(switches[60:80])
    print_result(switches[80:100])