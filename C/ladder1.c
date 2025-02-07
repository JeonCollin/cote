#include <stdio.h>

void move()
{
    

    for(int row = ar; row < 100; row++)
    {
        for(int col = 0; col < 100; col++)
        {

        }
    }
}

int main()
{   
    for(int t = 1; t <= 10; t++)
    {
        //테스트케이스 번호 받기
        int T;
        scanf("%d", &T);

        //사다리 행렬 받기
        int ladder[100][100] = {};

            //도착지점 기록
        int arriveX = 0, arriveY = 0;

        for(int i = 0; i < 100; i++)
        {
            for(int j = 0; j < 100; j++)
            {
                scanf("%d ", &ladder[i][j]);

                if(ladder[i][j] == 2)
                {
                    arriveY = i;
                    arriveX = j;
                }
            }
        }

        //알고리즘
        //방향벡터: 위, 왼, 오
        int dx[3] = {-1, 0, 0};
        int dy[3] = { 0,-1, 1};

        while(1)
        {
            //1순위: 왼쪽
            if()

            //2순위: 오른쪽

            //3순위: 위쪽
        }

        //결과출력
        printf("#%d %d", t, result);
    }

    return 0;
}