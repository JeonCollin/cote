def palindrome(string):

    L = len(string)

    for i in range(L):
        if(string[i] != string[L-1 - i]):
            return 0
    
    return 1

T = int(input())

for t in range(1, T+1):
    
    mystr = input()

    print(f'#{t} {palindrome(mystr)}')