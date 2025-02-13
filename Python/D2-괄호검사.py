def push(item):
    global top
    global N

    #일단 top 증가
    top += 1

    if(top == N):
        return 'overflow'
    
    #push하면 top에 값을 저장한다
    else:
        stack[top] = item

def pop():
    global top

    #underflow 고려
    if(top == -1):
        return 'underflow'
    
    #pop하면 top이 감소하고 값을 반환한다
    else:
        top -= 1
        return stack[top+1]

def test(string):

    #code를 순회하며 괄호 검사
    for i in range(N):

        #왼쪽 괄호라면 push
        if(string[i] == '(' or string[i] == '{'):
            push(string[i])

        #오른쪽 괄호라면 pop을 하는데
        if(string[i] == ')' or string[i] == '}'):

            comp = pop()
            #두 괄호가 다르다면 0출력
            if(comp == '{' and string[i] == ')'):
                return 0
            
            elif(comp == '(' and string[i] == '}'):
                return 0
            
            #underflow여도 0 출력
            elif(comp == 'underflow'):
                return 0
            
        #print(stack)
            
    #스택이 비어있지 않아도 0 출력
    if(top != -1):
        return 0

    #아무런 문제 없다면 1출력
    return 1

#########   main    ############

T = int(input())

for t in range(1, T+1):

    code = list(input())
    N = len(code)

    #스택 초기화
    stack = [0] * N
    top = -1

    print(f'#{t} {test(code)}')