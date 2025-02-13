#include <stdio.h>

char stack[1000];
int top = -1;

void stack_init()
{
    for(int i = 0; i < 1000; i++)
        stack[i] = '\0';
    top = -1;
}

void push(char alpha)
{
    //우선 top을 증가시킨다
    top += 1;

    //overflow는 발생 안함
    //write
    stack[top] = alpha;
}

int pop()
{
    //underflow
    if(top == -1)
        return -1;

    //pop
    else
    {
        //pop할 때 지우는 기능 추가
        stack[top] == '\0';
        top -= 1;
        return 0;
    }
}

int len(char *str)
{   
    //문자열 길이 구하는 함수
    int length = 0;

    while(str[length] != '\0')
        length ++;

    return length;
}



int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 0; t < T; t++)
    {

        //필요한 문자 받기
        char string[1000];
        scanf("%s ", &string);

        //문자열 길이 설정
        int length = len(string);

        //stack 초기화
        stack_init();

        for(int idx = 0; idx < length; idx++)
        {
            //이전에 push된 값과 동일하다면
            //이전 것도 pop시켜 지운다
            if(string[idx] == stack[top])
                pop();

            else
                push(string[idx]);
        }

        //결과 문자열 만들기
        int index = 0;

        while(stack[index] != '\0')
        {
            index ++;
        }
        
        printf("%s\n", stack);

        //결과 출력
        printf("#%d %d\n", t+1, index);
    }
    return 0;
}