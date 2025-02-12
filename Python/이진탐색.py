def binary_search(page, num):
    
    #파라미터 초기화
    start = 1
    end = page
    trial = 0

    while(start <= end):
        #선택지점 설정, 초기화
        middle = (start+end)//2
        trial += 1

        #찾는 수가 더 큰 경우 시작점을 오른쪽으로 이동
        if(middle < num):
            start = middle + 1

        #찾는 수가 더 작은 경우 끝점을 왼쪽으로 이동
        elif(middle > num):
            end = middle - 1

        #찾은 경우 걸린 횟수 리턴
        else:
            return trial


T = int(input())

for t in range(1, T+1):

    #PAB받기: P-책 페이지 수, A가 찾을 페이지, B가 찾을 페이지
    P, A, B = list(map(int, input().split()))

    trialA = binary_search(P, A)
    trialB = binary_search(P, B)

    #결과출력: 횟수가 더 적은 사람이 이김
    #A가 이긴 경우
    if(trialA < trialB):
        print(f'#{t} A')

    #B가 이긴 경우
    elif(trialB < trialA):
        print(f'#{t} B')

    else:
        print(f'#{t} 0')