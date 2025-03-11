T= int(input())

for t in range(1, T+1):
    
    # N: 돌아가야 할 학생 수
    N = int(input())
    
    # 학생 리스트 받기
    students = []
    for n in range(N):
        temp = list(map(int, input().split()))
        students.append(temp)
        
    # 학생의 시작 방과 끝 방을 인덱스로 삼아서
    # 통로에 경로를 칠하기
    # 방 번호는 1 ~ 400
    corridor = [0]*401
    
    # 복도를 색칠하자
    for i in range(len(students)):
        
        start = (students[i][0] + 1) // 2
        end = (students[i][1] + 1) // 2
        
        # 시작 / 끝을 색칠
        if(start < end):
            
            for j in range(start, end + 1):
                corridor[j] += 1
    
        # 시작점이 더 크면 반대로 색칠
        else:
            
            for j in range(end, start + 1):
                corridor[j] += 1
            
    # 겹친 최대 수를 출력
    # 결과 출력
    print(f'#{t} {max(corridor)}')