def count_num(mylist, num):
    # 리스트에서 해당 숫자의 개수를 세는 함수
    count = 0
    
    for i in range(len(mylist)):
        if(mylist[i] == num):
            count += 1

    return count

def max_num(mylist):
    # 리스트에서 최댓값을 찾아주는 함수
    max = mylist[0]

    for i in range(len(mylist)):
        if(mylist[i] >= max):
            max = mylist[i]
    return max

def delete_max(mylist, maxN):
    # 리스트에서 최대값을 제거하는 함수
    for i in range(len(mylist)):
        if(mylist[i] == maxN):
            mylist[i] = 0

    return mylist


# 총 N 라운드
N = int(input())

for n in range(1, N+1):

    # 별4 > 동그라미3 > 네모2 > 세모1
    # 카드 수, [카드리스트]
    myAlist = list(map(int, input().split()))
    Alist = myAlist[1:]
    myBlist = list(map(int, input().split()))
    Blist = myBlist[1:]

    win = ''

    while True:
        # print(Alist)
        # print(Blist)
        myAlist.sort()
        myBlist.sort()

        # 무승부: 둘이 똑같다
        if(Alist == Blist):
            win = 'D'
            break

        maxA = max_num(Alist)
        maxB = max_num(Blist)
        countA = count_num(Alist, maxA)
        countB = count_num(Blist, maxB)

        # 최대값이 큰 쪽이 이긴다
        if(maxA > maxB):
            win = 'A'
            break
        
        elif(maxA < maxB):
            win = 'B'
            break
        
        # 둘 다 최대 수가 같을 경우
        else:
            # 최대값이 많은 쪽이 이긴다
            if(countA > countB):
                win = 'A'
                break

            elif(countA < countB):
                win = 'B'
                break
            
            # 그것 마저 같으면
            else:
                # 최대값을 제외하고 다시 비교
                Alist = delete_max(Alist, maxA)
                Blist = delete_max(Blist, maxB)
                # print(Alist)
                # print(Blist)

    print(win)