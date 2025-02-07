#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
        //사람 수 입력
		int N;
        scanf("%d", &N);

        //사람의 소득 입력 + 평균내기
        int people[N];
        int sum = 0;

        for(int i = 0; i < N; i++)
        {
            scanf("%d ", &people[i]);
            sum = sum + people[i];
        }

        //평균과 비교
        int count = 0;
        
        for(int i = 0; i < N; i++)
        {
            if(people[i] <= sum/N )
                count = count + 1;
        }


		//결과 출력
		printf("#%d %d\n", t, count);
	}
	return 0;
}
