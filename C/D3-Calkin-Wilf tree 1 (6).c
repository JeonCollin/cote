#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        int bit[50];
        scanf("%50s", &bit);
        printf("bit: %s\n", bit);
        
        int length = (int)sizeof(bit)/sizeof(bit[0]);
        printf("length: %d", length);

        int count = 0;
        
        //수를 다 뒤집을려면 바로 붙어있는 애들은 신경 안쓰고 0101처럼 떨어진 애들은 신경 써줘야함
        for(int i = 0; i < length; i++)
        {
            //이웃한게 다른 수면 count + 1
            if(bit[i] != bit[i+1])
                count += 1;
        }

        printf("#%d %d\n", t, count);
    }
    return 0;
}