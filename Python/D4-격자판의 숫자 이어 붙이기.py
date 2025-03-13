# 상 하 좌 우
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
    
def dup_permutation(idx):
    
    # 중복순열 완성
    if(idx == r):
        # 중복순열 리스트에 추가
        PI_list.append(PI[:])
        
    else:
        # 중복순열 만들기
        for i in range(n):
            # 원소 선택
            PI[idx] = temp_list[i]
            dup_permutation(idx+1)
    
def move(row, col):
    
    # 초기화
    word = mylist[row][col]
    ROW = row
    COL = col
    result = []
    out_of_range = False
    
    # 존재하는 중복순열만큼 반복
    for i in range(len(PI_list)):
        # 적힌 대로 이동한다
        for j in range(6):
            
            ROW += drow[PI_list[i][j]]
            COL += dcol[PI_list[i][j]]
            
            # 범위를 벗어나면 다음 순열로 넘어간다
            if(0 > ROW or 4 <= ROW or 0 > COL or 4 <= COL):
                word = mylist[row][col]
                out_of_range = True
                break
            
            # 범위를 벗어나지만 않으면 괜찮다
            word += mylist[ROW][COL]
        
        # 범위를 벗어나면 다음 순열로 넘어간다
        if(out_of_range == True):
            out_of_range = False
            continue
        
        # 숫자열이 완성되었으면 추가한다
        result += word
        
        # 다음 루프를 위해 초기화
        word = mylist[row][col]
        ROW = row
        COL = col
        
    return result
            


T = int(input())

for t in range(1, T+1):
    
    mylist = [list(map(str, input().split())) for _ in range(4)]
    
    # 중복순열 초기화
    temp_list = [0,1,2,3]
    n = 4
    r = 6
    PI = [0]*r
    PI_list = []
    dup_permutation(0)
    # 만들어진 글자들 저장
    words = []
    
    # 시작점을 정하고 가능한 모든 경우를 살펴보자
    for row in range(4):
        for col in range(4):
            # 이동 알고리즘 적용
            words.append(move(row, col))
    
    
    # 중복 제거
    print(words)
    set_words = set(words)
    
    # 다시 리스트로 만들어서 전체 개수 구하기
    last = list(set_words)
    
    # 결과 출력
    print(f'#{t} {len(last)}')
    

'''
상하좌우로 이루어진 중복순열
범위를 벗어나지 않게 제한하면 된다
상상상상상상상: 불가능

시간복잡도: 모든 행,렬 = 16
중복순열: 4^7: 16834
'''