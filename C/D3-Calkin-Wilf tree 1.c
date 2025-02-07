#include <stdio.h>
#include <string.h>

// 왼쪽일 경우, b가 증가
void Left(int* a, int* b)
{
    *b = *b + *a;
}

// 오른쪽일 경우 a가 증가
void Right(int* a, int* b)
{
    *a = *b + *a;
}


int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//문자열 받기
        char LR[30];
        scanf("%s", &LR);

        //왼쪽 오른쪽 알고리즘
        int a = 1, b = 1;

        for(int i = 0; i < strlen(LR); i++)
        {
            if(LR[i] == 'L')
                Left(&a, &b);

            else
                Right(&a, &b);
        }

		//결과 출력
		printf("#%d %d %d\n", t, a, b);
	}
	return 0;
}


