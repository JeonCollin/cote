#include<stdio.h>

void sort(int member[], int N)
{
	//키가 작은 순서대로 정렬        
	for(int r = 0; r < N; r ++)
    {
    	for(int c = 0; c < N; c++)
        {
            int temp;
            
            if(r < c)
            {
          		//swap
       			if(member[r] > member[c])
          		{
                	temp = member[c];
                	member[c] = member[r];
                	member[r] = temp;
            	}
        	}
    	}
    }
}


int main()
{
	int T;
    scanf(&quot;%d&quot;, &T);

	for(int test_case = 1; test_case <= T; ++test_case)
	{	
        // N은 점원 수	B는 빌딩 길이
		int N, B; 
        scanf(&quot;%d %d&quot;, &N, &B);
        
        //검증용
        //printf(&quot;B: %d\n&quot;, B);
        
        //점원 입력
        int member[N];
        
        for(int i = 0; i < N; i++)
        {
        	scanf(&quot;%d &quot;, &member[i]);
        }
        
        // 검증용
        /*for(int i = 0; i < N; i++)
        {
        	printf(&quot;%d &quot;, member[i]);
        }
        printf(&quot;\n&quot;);*/
        
        //점원 키의 합
        int sum = 0;
        for(int i = 0; i < N; i ++)
        {
        	sum = sum + member[i];
        }
        
        while(1)
        {
            //합에서 비교
        	int differ = sum - B;
            
            //키가 작은 순서대로 정렬    
        	sort(member, N);
            
            //differ보다 작으면서 가장 가까운 수의 인덱스 탐색
            int index = 0, check = N;
            
            for(int i = N-1; 0 <= i; i--)
            {
            	if(differ >= member[i])
                {
                	index = i;
                    check = check - 1;
                    break;
                }
            }
            
            //처음부터 작은 수 자체가 없었다면 끝
            if(check == N)  break;
            
            //더이상 differ보다 작은 수가 없다면 끝
            if(member[index] == 0)  break;
            
            //differ가 0보다 작으면 끝
            if(differ < 0)  continue;
            
            //differ가 0이면 끝
            if(differ == 0)  break;
            
            //differ보다 작으면서 가장 가까운 수를 뺌
            sum = sum - member[index];
            member[index] = 0;
            
        }
        
		//결과출력
        printf(&quot;#%d %d\n&quot;, test_case, sum - B);
        
    }
    
	return 0; //정상종료시 반드시 0을 리턴해야합니다.
    
}