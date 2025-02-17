def push(item):
    global top
    global N
    # 일단 top 증가
    top += 1

    # overflow
    if(top == N):
        print('overflow')

    else:
        stack[top] = item

def pop():
    global top

    # underflow
    if(top == -1):
        return False

    else:
        top -= 1
        return stack[top+1]
    
def calculator(mylist):
    
    


T = int(input())

for t in range(1, T+1):

    # 일단 후위 표기법을 받자
    mylist = list(input().split())
    N = len(mylist)

    # 스택 초기화
    stack = ['']*N
    top = -1

    # 스택에 문자열 넣기
    for i in range(N):
        push(mylist[i])