#include <stdio.h>

int main()
{
	int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; t++)
    {
        //문자열 길이 N
        int N;
        scanf("%d", &N);

        //정답 문자
        char correctString[N+1];
        scanf("%s", &correctString);

        //석찬련이 쓴 문자
        char myString[N+1];
        scanf("%s", &myString);

        int correctNum = 0;

        for(int i = 0; i < N; i++)
        {
            if(correctString[i] == myString[i])
                correctNum += 1;
        }
        
        //결과 출력
    	printf("#%d %d\n", t, correctNum);
    }
    return 0;
}