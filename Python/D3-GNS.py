GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

def counting_list(arr):
    global GNS
    global N

    #0 ~ 9
    count_list = [0]*10

    #외계어를 순회한다
    for i in range(N):

        #우리나라 말을 순회한다
        for index in range(len(GNS)):

            #외계어를 우리 말로 번역한다
            if(GNS[index] == arr[i]):
                count_list[index] += 1

    #카운트리스트를 누적합한다
    for i in range(1, 10):
        count_list[i] += count_list[i-1]

    #카운트를 까면서 다시 외계어를 sort한다
    result_list = ['']*N

    #원래 배열을 순회하며 카운트를 깐다
    for i in range(N):
        
        for j in range(len(GNS)):

            if(arr[i] == GNS[j]):
                count_list[j] -= 1
                result_list[count_list[j]] = arr[i]

    return result_list


T = int(input())

for t in range(1, T+1):

    mylist = list(input().split())

    N = int(mylist[1])

    #alien = [svn, for, zro, ...]
    alien = list(input().split())

    result = ' '.join(counting_list(alien))

    print(f'#{t} {result}')