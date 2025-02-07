#include <stdio.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//N
        int N;
        scanf("%d", &N);

        //장애물 리스트 받기
        int huddle[N];

        for(int i = 0; i < N; i++)
        {
            scanf("%d ", &huddle[i]);
        }

        //장애물 차이 구하기
        int downMin = 0, upMax = 0;

        for(int i = 0; i < N-1; i++)
        {
            int difference = huddle[i+1] - huddle[i];

            if(difference >= 0)
            {
                if(difference >= upMax)
                
                    upMax = difference;
            }

            if(difference <= 0)

                if(difference < downMin)
                    downMin = difference;
        }

		//결과 출력
		printf("#%d %d %d\n", t, upMax, -downMin);
	}
	return 0;
}


