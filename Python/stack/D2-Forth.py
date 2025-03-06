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
    
    L = len(mylist)

    # 문자열을 순회하며 연산자/피연산자 확인
    for i in range(L):

        # print(stack)
        # print(mylist[i])

        # 숫자라면 push
        if(mylist[i].isdigit() == True):
            push(int(mylist[i]))

        # 끝인 .에 도달했으면 끝
        elif(mylist[i] == '.'):
            return pop()

        # 연산자면 pop
        else:
            num1 = pop()
            num2 = pop()

            # 숫자나 연산자가 남으며 에러
            if(num1 == False or num2 == False):
                return 'error'

            # 나중에 나온 수가 앞으로 가야 함
            # 연산 결과를 다시 push한다
            if(mylist[i] == '+'):
                push(num2 + num1)

            elif(mylist[i] == '-'):
                push(num2-num1)
            
            elif(mylist[i] == '*'):
                push(num2*num1)
            
            elif(mylist[i] == '/'):
                push(num2//num1)
            


T = int(input())

for t in range(1, T+1):

    # 일단 후위 표기법을 받자
    mylist = list(input().split())
    N = len(mylist)

    # 스택 초기화
    stack = ['']*N
    top = -1

    # 결과 출력
    print(f'#{t} {calculator(mylist)}')

    
