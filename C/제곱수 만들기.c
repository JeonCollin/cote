#include <stdio.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//A를 받고 루트A 이상부터 num을 제곱을 시켜서 A*B랑 같으면 되지 않을까?
        int A, B;

        for(B = 1; B <= A; B++)
        {
            if((double)sqrt(A*B) == (int) sqrt(A*B))
                break;
        }

		//결과 출력
		printf("#%d %d\n", t, B);
	}
	return 0;
}
