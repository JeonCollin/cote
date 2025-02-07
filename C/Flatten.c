#include <stdio.h>

int main()
{
	for(int t = 1; t <= 10; t++)
	{
        //덤프 횟수 받기
        int dump;
	    scanf("%d", &dump);

        //상자의 높이들을 받기
        int box[100] = {};

        for(int i = 0; i < 100; i++)
        {
            scanf("%d ", &box[i]);
        }

		//알고리즘, 카운팅배열을 쓴다면?

        //파라미터 설정
        int count_list[101] = {}; // 카운트리스트는 0~100까지임
        int left = 1, right = 100; // 조건에 따라 인덱스 시작도 1~100임
        int minpoint = 1, maxpoint = 100;

        //상자의 높이를 카운팅하면, 카운팅 배열에서 가장 왼쪽 최솟값
        //가장 오른쪽이 최대값
        //dump는 최대값 카운트 -1, 그 직전 값 카운트 +1
        //최대값 카운트 -1, 그 다음 최소값 카운트 +1

        //count_list 만들기: box는 0~99까지임
        for(int i = 0; i < 100; i++)
        {
            count_list[box[i]] += 1;
        }

        //count list에서 dump하기
        for(int i = 0; i < dump; i++)
        {   
            //최소지점 찾기
            while(1)
            {
                if(count_list[left] > 0 && left <= 100)
                {
                    minpoint = left;
                    break;
                }
                left += 1;
            }

            //최대지점 찾기
            while(1)
            {
                if(count_list[right] > 0 && right >= 0)
                {
                    maxpoint = right;
                    break;
                }
                right -= 1;
            }

            //평탄화가 완료되었을 경우 종료
            if(maxpoint == minpoint || maxpoint - minpoint == 1)
                break;

            //dump
            //최대지점 카운트 -1, 그 이전 지점 카운트 +1
            count_list[maxpoint] -= 1;
            count_list[maxpoint-1] += 1;

            //최소지점 카운트 -1, 그 다음 지점 카운트 +1
            count_list[minpoint] -= 1;
            count_list[minpoint+1] += 1;
        }

		//결과 출력
		printf("#%d %d\n", t, maxpoint - minpoint);
	}
	return 0;
}