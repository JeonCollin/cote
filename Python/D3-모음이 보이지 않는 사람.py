T = int(input())

for t in range(T):

    #알파벳 받기
    alpha = list(input())

    #모음을 제거한 알파벳리스트 만들기
    result = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(alpha)):

        if alpha[i] not in vowels:
            result =result + str(alpha[i])

    print(f'#{t+1} {result}')