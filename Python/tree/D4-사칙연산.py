def post_order(n):
    # 후위 계산법
    # 좌, 우, 현재
    # 노드의 최대까지 도달하면 끝
    if(n <= N):
        # 좌
        # post_order(left[n])
        # # 우
        # post_order(right[n])
        # 현재
        if(tree[n] == '+'):
            return post_order(left[n]) + post_order(right[n])


        elif(tree[n] == '-'):
            return post_order(left[n]) - post_order(right[n])


        elif(tree[n] == '*'):
            return post_order(left[n]) * post_order(right[n])


        elif(tree[n] == '/'):
            return  post_order(left[n]) // post_order(right[n])


        # 숫자면 값을 리턴
        else:
            return tree[n]



        


for t in range(1, 11):

    N = int(input())

    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)

    # N 줄에 걸쳐 노드와 간선의 정보를 받는다
    for n in range(1, N+1):

        mylist = list(input().split())

        L = len(mylist)

        # 좌, 우, 연산자가 주어진 경우
        if(L == 4):
            tree[n] = mylist[1]
            left[n] = int(mylist[2])
            right[n] = int(mylist[3])
        
        # leaf인 경우는 숫자만 받는다
        else:
            tree[n] = int(mylist[1])

    # 노드별 숫자/연산자와 연결 정보 완성

    # 연산하자
    result = post_order(1)
    
    # 결과 출력
    print(f'#{t} {result}')