stack = ['']*1000
top = -1

def my_push(alpha):
    
    global top

    #우선 top을 증가시킨다
    top += 1
    #overflow는 없을 것이다
    #write
    stack[top] = alpha

def my_pop():

    global top

    #underflow
    if(top == -1):
        return False
    
    #pop
    else:
        #pop할 때 지우는 값으로 ''할당
        stack[top] = ''
        top -= 1
        return stack[top+1]
        

T = int(input())

for t in range(1, T+1):

    #문자를 입력받아서 리스트로 만들기
    strlist = list(input())

    for idx in range(len(strlist)):

        #만약 이전에 push된 값과 동일하다면 
        #이전 것도 pop하고 지운다
        if(strlist[idx] == stack[top]):
            my_pop()

        else:
            my_push(strlist[idx])

    #결과 문자열 만들기
    index = 0
    result_str = ''

    while(stack[index] != ''):
        result_str += stack[index]
        index += 1

    #결과출력
    print(f'#{t} {len(result_str)}')

    #스택 초기화
    stack = ['']*1000
    top = -1