#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		int A, B;
        scanf("%d %d", &A, &B);

        int time;

        if(A+B >= 24)
            time = A + B - 24;

        else
            time = A + B;
        
		//결과 출력
		printf("#%d %d\n", t, time);
	}
	return 0;
}
