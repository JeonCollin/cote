def dup_combination(idx, start):

    # nHr 구현
    # 원하는 원소 수 r개를 선택했다면
    if(idx == r):
        # 원하는 작업을 수행
        print(H)

    else:
        # 조합을 선택
        # 중복 허용
        for i in range(start, N):
            # 해당 원소를 조합에 넣는다
            H[idx] = mylist[i]
            # 해당 원소부터 원소를 선택한다
            dup_combination(idx+1, i)

mylist = [1,2,3,4,5,6]
N = 6
r = 3
H = [0]*r
dup_combination(0,0)