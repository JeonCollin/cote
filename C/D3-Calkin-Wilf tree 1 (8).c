#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		int N;
        scanf("%d", &N);

		//결과 출력
		printf("#%d %d\n", t, N/3);
	}
	return 0;
}
