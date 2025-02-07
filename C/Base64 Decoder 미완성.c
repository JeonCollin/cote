#include <stdio.h>
#include <string.h>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++)
	{
		//알고리즘
        //T, G... >> 19, 6... >> 010011 000110... >>01001100 0110... >> 76 ... >> L ...

        char string[100000];
        fgets(string, sizeof(string), stdin);
        input[strcspn(input, "\n")] = '\0';

        int length = strlen(string);

        int encodingNum[length];
        int combineBin[100000];

        //1. 입력받은 문자를 표에 따라 값으로 바꾸기 >> 6비트 이진수로 바꾸기
        for(int i = 0; i < length; i++)
        {
            toBinary6((int)string[i] - 'A', encodingNum[i]);
        }
        
        //2. 6비트 이진수를 8비트로 끊어서 아스키코드로 변환
        //6비트 이진수를 이어 붙이기
        for(int i = 0; i < length; i++)
        {
            strcat(combineBin, encodingNum[i]);
        }

        

		//결과 출력
		printf("#%d %d\n", t, ?);
	}

	return 0;
}
