#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
        //N받기
        int N;
        scanf("%d", &N);
         
        //숫자 리스트 받기
        int arr[N];
        for(int i = 0; i < N; i++)
            scanf("%d ", &arr[i]);
        
		//알고리즘
        //최대최소 초기화
        int max = arr[0], min = arr[0];
        
        //리스트를 순회하며 최대최소 구하기
        for(int i = 0; i < N; i++)
        {
        	if(arr[i] > max)
                max = arr[i];
            
            if(arr[i] < min)
                min = arr[i];
        }

		//결과 출력
		printf("#%d %d\n", t, max - min);
	}
	return 0;
}