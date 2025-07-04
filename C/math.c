#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//定義
/* 
   このように複数行
   コメント可能です。
*/
#define PI 3.14  
int main(int argc,char** argv){
    int a,b;
    // 乱数の初期化 シードを設定しないと、毎回同じ「乱数」が生成されてしまいます。
    // time(NULL) 現在時刻のエポック秒を返す 1970年1月1日から
    srand( time(NULL));
    //	１から１０までの乱数を発生させる
    a = rand() % 10 + 1;
    b = rand() % 10 + 1;
    //	計算結果を出力
    printf("%d + %d = %d\n",a,b,a+b);



    return 0;
}