#include <stdio.h>

int biggerThan10(A, B)
{
    if (A >= 10 || B >= 10)
        return -1;

    else
    {
        return A*B;
    }
}

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//AB입력
        int A, B, result;
        scanf("%d %d", &A, &B);

        result = biggerThan10(A, B);

		//결과 출력
		printf("#%d %d\n", t, result);
	}
	return 0;
}


