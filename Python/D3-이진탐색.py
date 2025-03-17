def binary_search(arr, start, end, target):
    # 재귀함수여서 리턴해도 의미가 없다
    global cnt
    # 종료조건: 끝점 < 시작점
    if(end < start):
        return False
    
    # 그 전까지는 검색
    else:
        mid = (start + end)//2
        # 현재 수가 찾으려는 수보다 작다
        if(target > arr[mid]):
            # 시작점 조정
            binary_search(arr, mid+1, end, target)
        
        # 현재 수가 찾으려는 수보다 크다
        elif(target < arr[mid]):
            # 끝점 조정
            binary_search(arr, start, mid-1, target)
            
        # 찾았으면 정상리턴
        else:
            cnt += 1
            return True
     

T = int(input())

for t in range(1, T+1):
    
    # N개의 정수를 리스트 A에 저장한다
    N, M = list(map(int, input().split()))
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 지 확인한다
    cnt = 0
    
    for m in range(M):
        temp = binary_search(A, 0, N-1, B[m])

    
    # 결과 출력
    print(f'#{t} {cnt}')