#include <stdio.h>
//gcc HelloWorld_c.c -o HelloWorld_c.exe
int main() {
    //\n 改行
    char userName[100];
    printf("Please enter your name:"); 
    scanf_s("%99s", userName); 
    printf("Hello, %s!\n", userName); 
    return 0;
} 