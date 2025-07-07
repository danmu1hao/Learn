#include <stdio.h>

// ポインタの基本的な使い方を示すサンプル
int main() {
    int a=100;
    int* p;//ポインター
    p=&a;
    *p=1;
    *(&a)=1;//上同じ
    // ポインタを使って値を出力
    printf("aの値: %d\n", a); // 直接aの値を表示
    printf("pが指す値: %d\n", *p); // ポインタを使ってaの値を表示
    printf("aのアドレス: %p\n", (void*)&a); // aのアドレスを表示
    printf("pの値（アドレス）: %p\n", (void*)p); // pの値（アドレス）を表示
    return 0;
}
