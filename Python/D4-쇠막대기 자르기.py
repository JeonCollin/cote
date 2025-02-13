stack = [''] * 100000
top = -1

def stack_init():
    global top
    global stack

    stack = [''] * 100000
    top = -1

def push(item):
    global top

    #일단 top 증가
    top += 1

    #overflow는 생각 안함
    if(top == 100000):
        return 'overflow'
    
    #write
    else:
        stack[top] = item

def pop():
    global top
    #underflow 생각
    if(top == -1):
        return 'underflow'
    
    #Read
    else:
        top -= 1
        return stack[top+1]

T = int(input())

for t in range(1, T+1):

    #스택 초기화
    stack_init()

    #문자열 입력을 리스트로 나눈다
    pipes = list(input())

    #문자열 길이
    L = len(pipes)

    #총 파이프 수
    sum_pipes = 0

    #입력받은 문자열을 순회하며
    for idx in range(L):
        
        #여는 괄호면 push
        if(pipes[idx] == '('):
            push(pipes[idx])

        #닫는 괄호면 pop
        if(pipes[idx] == ')'):
            
            #레이저로 쪼개질 때
            if(pipes[idx-1] == '('):
                sum_pipes += top
                pop()

            #그냥 파이프가 끝날 때
            if(pipes[idx-1] == ')'):
                sum_pipes += 1
                pop()
        

    #결과출력
    print(f'#{t} {sum_pipes}')

'''
(): 레이저: 괄호가 바로 닫히는 애
( ): 쇠막대기: 괄호 안에 뭔가 있다. nest됨

() ( ( ( () () ) ( () ) () ) ) ( () )

레이저(((레이저레이저)(레이저)레이저))(레이저)

레이저를 지금 level을 더해주는 걸로 생각해보자

레이저 ( ( ( 레이저 레이저 ) ( 레이저 ) 레이저 ) ) ( 레이저 )
level = top + 1
level: 1 2 3             2 3        2       1 0 1        0
누적:       3 + 3 / 3+3 + 3 / 3+3+3 + 3 /3+3+3+3 + 2 / 3+3+3+3+2 + 1
실제:    3      6     9        13        15         17

)( 하나당 +1을 하면 될듯?

결론: 레이저는 level을 더한다. )(는 +1 해준다
레이저의 괄호는 제외하고 생각한다

( ( ( 레이저 ( 레이저 레이저 ) ) ( 레이저 ) 레이저 ) ) ( 레이저 레이저 )

'''