#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//K N M 받기
        int K, N, M;
        scanf("%d %d %d", &K, &N, &M);

        //충전소 정류장 번호 받기
        int charger[M];
        for(int i = 0; i < M; i++)
        {
            scanf("%d ", &charger[i]);
        }



        //충전소 간 거리를 측정한 새로운 리스트 생성하기
        int distance[M+1];

        for(int i = 0; i < M + 1; i++)
        {
            if(i == M)
                distance[i] = N - charger[M-1];

            else if(i == 0)
                distance[i] = charger[0];

            else
                distance[i] = charger[i] - charger[i-1];
        }
        

        //파라미터 초기화
        int sum = 0;
        int stay = 0;

        //거리 리스트를 순회하며 요소를 더한다
        for(int i = 0; i < M + 1; i++)
        {
            //만약 요소 자체가 K보다 크면 그냥 끝내고 stay = 0이 된다
            if(distance[i] > K)
            {
                stay = 0;
                break;
            }

            sum = sum + distance[i];
            //만약 합이 K 초과면 카운팅하고 현재 거리차로 초기화 한다.
            if(sum > K)
            {
                stay += 1;
                sum = distance[i];
            }
            
        } 

        //결과출력
		printf("#%d %d\n", t, stay);
	}
	return 0;
}

/*
0에서 시작 N에서 끝남
시작점, 중간 충전소, 도착점간의 차이가 K이하

charger:   1 3 5 7 9
distance: 1 2 2 2 2 1
sum:        0   0   0
stay:       1   1   1

 1 3 7 8 9
1 2 4 1 1 1

5 20 5
charger:   4 7 9 14 17
distance: 4 3 2 5  3  3
sum:        0 0   0
stay:       1 1   1
*/