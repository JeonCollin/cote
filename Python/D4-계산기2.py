def push(item):
    global top

    top += 1

    # overflow
    if(top == N):
        print('overflow')

    # push
    else:
        stack[top] = item

def pop():
    global top

    # underflow
    if(top == -1):
        return False
    
    # pop
    else:
        top -= 1
        return stack[top+1]
    
def change_to_back(mystr):
    # 후위 표기법으로 바꿔주는 함수
    global top
    result = ''

    for i in range(len(mystr)):
        # print(stack)
        # print(mystr[i])
        # print(mystr[i].isdigit())
        # 숫자면 그냥 더한다
        if(mystr[i].isdigit() == True):
            result += mystr[i]

        # 연산자면 생각을 해아함
        # 가장 처음에 나오는 연산자는 push
        elif(mystr[i].isdigit() == False and top == -1):
            push(mystr[i])
            # 그 뒤에 나오는 연산자는 우선순위를 비교해야 함
        
        # *가 +보다 우선순위가 높다
        # top이 *인데 +를 만나면 pop하고 나서 push
        # top이 +인데 +를 만나도 pop하고 나서 push
        elif(mystr[i] == '*'):
            push(mystr[i])

        elif(mystr[i] == '+'):
            
            while True:

                oper = pop()
                
                # *라면 +가 나올 때 까지 pop한다
                if(oper == '*' and top != -1):
                    result += oper
                
                # +라면 문자열에 더하고
                # 지금 연산자를 push한다
                else:
                    result += oper
                    push(mystr[i])
                    break
        
        # 문자열 끝부분이면 모두 pop
        elif(mystr[i] == '.'):
            
            while(top != -1):
                result += pop()

    return result

def calculate(word):
    # 후위표기법을 계산하는 함수

    for i in range(len(word)):

        # 숫자라면 push
        if(word[i].isdigit() == True):
            push(int(word[i]))

        # 마지막 지점이라면 결과를 반환
        elif(word[i] == '.'):
            return pop()

        # 연산자라면 숫자 2개를 pop하고
        # 계산하고 나서 다시 push
        elif(word[i] == '*'):
            num1 = pop()
            num2 = pop()
            push(num2 * num1)

        elif(word[i] == '+'):
            num1 = pop()
            num2 = pop()
            push(num2 + num1)



for t in range(1, 11):

    # N 받기
    N = int(input())

    # 문자열 받기
    mystr = input()
    # 끝 부분을 알 수 있게 표시
    mystr += '.'

    # 스택초기화
    stack = ['']*N
    top = -1

    # 후위 표기법으로 바꾼다
    back_word = change_to_back(mystr)
    # 끝 부분을 알 수 있게 표시
    back_word += '.'

    # 스택초기화
    stack = [0]*N
    top = -1

    result = calculate(back_word)
    #print(back_word)

    # 결과출력
    print(f'#{t} {result}')