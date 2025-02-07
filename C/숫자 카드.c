#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
        //N 받기
		int N;
        scanf("%d", &N);

        //카드를 문자열로 받기
        char card[N];
        scanf("%s", &card);

        //알고리즘

        //숫자를 저장할 배열 생성
        int numArr[10] = {};

        for(int i = 0; i < N; i++)
        {
            //맨 앞 자리부터 숫자를 빼오고, 카운팅한다
            numArr[(int) card[i] - '0'] += 1;
        }

        //배열을 순회하며 최대값과 그 수 찾기
        int max = 0;
        int index = 0;

        for(int i = 0; i < 10; i++)
        {
            if(numArr[i] >= max)
            {   
                //max가 장 수
                max = numArr[i];
                //인덱스가 카드 값
                index = i;
            }
        }

		//결과 출력
		printf("#%d %d %d\n", t, index, max);
	}
	return 0;
}
