#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
        // L <= X <= U
        int L, U, X;
        scanf("%d %d %d", &L, &U, &X);

        //운동시간 판단
        int restTime;

        if(X > U)
            restTime = -1;

        else if (L > X)
            restTime = L - X;

        else               
            restTime = 0;

		//결과 출력
		printf("#%d %d\n", t, restTime);
	}
	return 0;
}
