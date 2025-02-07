#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//알고리즘
        int N;
        scanf("%d", &N);

        int a = 0, b = 0, c = 0, d = 0, e = 0;

        while(1)
        {
            if(N%2 == 0)
            {
                a += 1;
                N = N/2;
            }

            if(N%3 == 0)
            {
                b += 1;
                N = N/3;
            }

            if(N%5 == 0)
            {
                c += 1;
                N = N/5;
            }

            if(N%7 == 0)
            {
                d += 1;
                N = N/7;
            }

            if(N%11 == 0)
            {
                e += 1;
                N = N/11;
            }    

            if(N == 1)
                break;

        }

		//결과 출력
		printf("#%d %d %d %d %d %d\n", t, a, b, c, d, e);
	}
    
	return 0;
}
