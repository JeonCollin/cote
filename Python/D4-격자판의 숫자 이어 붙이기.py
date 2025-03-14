'''
상하좌우로 이루어진 중복순열
범위를 벗어나지 않게 제한하면 된다
상상상상상상상: 불가능

시간복잡도: 모든 행,렬 = 16
중복순열: 4^7: 16834
'''

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
    # 만들어진 순열에 따라 이동시켜주는 함수
    
    # 결과
    result = []
    
    # 특정 순열을 정한다
    for i in range(len(PI_list)):
        # 초기화
        ROW = row
        COL = col
        word = mylist[row][col]
        
        # 특정 순열을 정했으면 그 순열대로 움직인다
        for j in range(len(PI_list[i])):
            ROW = ROW + drow[PI_list[i][j]]
            COL = COL + dcol[PI_list[i][j]]
            
            # 범위를 벗어나지 않으면 숫자열 갱신
            if(0 <= ROW < 4 and 0 <= COL <4):
                word += mylist[ROW][COL]
            
            # 범위를 벗어나면 컷
            else:
                break
            
        # print(word)
        # 7글자가 완성되면 결과에 추가
        if(len(word) == 7):
            result.append(word)
            
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
            words += move(row, col)
    
    
    # 중복 제거
    #print(words)
    set_words = set(words)
    
    # 다시 리스트로 만들어서 전체 개수 구하기
    last = list(set_words)
    
    # 결과 출력
    print(f'#{t} {len(last)}')