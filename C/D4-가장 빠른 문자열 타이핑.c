#include <stdio.h>
#include <string.h>

int typing(char *str1, char *str2)
{
    //str1 = A
    //str2 = B

    int a = strlen(str1);
    int b = strlen(str2);

    int cnt = 0;
    int copy = 0;

    //기준 문자열: a
    for(int i = 0; i < a-b+1; i++)
    {
        //length 초기화
        int length = 0;

        //b와 동일한지 확인
        for(int j = 0; j < b; j++)
        {
            //다르면 끝
            if(str1[i+j] != str2[j])
                break;

            length += 1;
        }

        //동일한 문자가 있었다면 그 문자열 자체의 길이를 센다
        if(length == b)
        {
            for(int idx = 0; idx < b; idx++)
            //string은 작은 따옴표를 쓴다
                str1[i+idx] = ' ';
                copy += 1;
            cnt += 1;
        }
        

    }
    // /////검증용//////
    // printf("%s\n", str1);
    // printf("%d\n", copy);
    // printf("%d\n", cnt);
    
    return a - cnt*b + cnt;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        char A[10000];
        char B[100];

        scanf("%s ", &A);
        scanf("%s ", &B);

        //결과 출력
        printf("#%d %d\n", t, typing(A, B));
    }
    return 0;
}