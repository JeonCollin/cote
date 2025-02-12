#include<stdio.h>

int main()
{
	int T;
    scanf("%d", &T);

	for(int test_case = 1; test_case <= T; ++test_case)
	{	
        // N은 점원 수	B는 빌딩 길이
		int N, B; 
        scanf("%d %d", &N, &B);
        
        //검증용
        //printf("B: %d\n", B);
        
        //점원 입력, 최솟값을 모든 점원의 키로 초기화
        int member[N];
        int min = 0;

        for(int i = 0; i < N; i++)
        {
        	scanf("%d ", &member[i]);
            min += member[i];
        }

        //부분집합에서 확인
        //모든 부분집합의 개수
        for(int i = 0; i < 1<<N ; i++)
        {   
            //특정 조합을 확인 후 sum 초기화
            int sum = 0;

            //특정한 부분집합이 선택됨
            for(int j = 0; j < N; j++)
            {
                //특정한 원소가 선택됨
                if(i & (1 << j))
                {
                    sum += member[j];
                }
            }

            //특정 조합 확인 후 최소값 갱신
            if(sum >= B && min >= sum)
                min = sum;
        }        
        
		//결과출력
        printf("#%d %d\n", test_case, min - B);
        
    }
    
	return 0; //정상종료시 반드시 0을 리턴해야합니다.
    
}