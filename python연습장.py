def combination(idx, start):

    # nCr 구현
    # 원하는 원소 수 r개를 선택했다면
    if(idx == r):
        # 원하는 작업을 수행
        print(C)

    else:
        # 조합을 선택
        for i in range(start, N):
            # 해당 원소를 조합에 선택한다
            C[idx] = mylist[i]
            # 해당원소 이후 원소를 선택한다
            combination(idx+1, i+1)

mylist = [1,2,3]
N = 3
r = 2
C = [0]*r

combination(0,0)
