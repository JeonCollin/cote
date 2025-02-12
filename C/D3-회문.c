#include <stdio.h>

//배열을 함수로 받을 때는 주소 연산자로 받아야 함
//배열 이름자체가 이미 주소여서그럼
int is_palindrome(char *alpha_list, int L)
{
    //회문인지 아닌지 검사하는 함수
    //특정 문자열을 받아서 앞뒤로 비교한다

    for(int i = 0; i < L; i++)
    {
        if(alpha_list[i] != alpha_list[L-1 -i])
            return 0;
    }
    return 1;
}

//2차원 배열을 함수로 받을 때는
// [][여기] 길이를 반드시 지정해줘야 함
int arr_to_word(char myarr[8][8], int L)
{
    int cnt = 0;

    for(int i = 0; i < 8; i++)
    {
        for(int j = 0; j < 8-L + 1; j++)
        {
            char arr_row[L];
            char arr_col[L];

            for(int l = 0; l < L; l++)
            {
                arr_row[l] = myarr[i][j+l];
                arr_col[l] = myarr[j+l][i];
            }

            if(is_palindrome(arr_row, L) == 1)
                cnt += 1;
            if(is_palindrome(arr_col, L) == 1)
                cnt += 1;
        }
    }
    return cnt;
}



int main()
{
    //10개의 테스트케이스
    for(int t = 1; t <= 10; t++)
    {
        //회문 길이 받기
        int L;
        scanf("%d ", &L);

        //글자 배열 받기
        char arr[8][8];

        for(int i = 0; i < 8; i++)
        {
            for(int j = 0; j < 8; j++)
            {   
                //문자열은 반드시 개행문자 제거해줘야 함
                scanf("%c ", &arr[i][j]);
            }
        }
        
        //결과출력
        printf("#%d %d\n", t, arr_to_word(arr, L));
    }
    return 0;
}