#include <stdio.h>
#include <string.h>

int main()
{
	int T;
	scanf("%d", &T);
    getchar();

	for(int t = 1; t <= T; t++)
	{
		//알파벳 받기
        char alpha[50] = {};
        fgets(alpha, sizeof(alpha), stdin);
        //printf("%s", alpha);
        
        //모음을 제거한 새로운 알파벳 리스트 만들기
        char result[50] = {};
        int idx = 0;

        for(int i = 0; i < strlen(alpha); i++)
        {
            if(alpha[i] != 'a' && alpha[i] != 'e' && alpha[i] != 'i' && alpha[i] != 'o' && alpha[i] != 'u')
            {
                result[idx] = alpha[i];
                idx ++;
            }
        }

		//결과 출력
		printf("#%d %s", t, result);
	}
	return 0;
}


