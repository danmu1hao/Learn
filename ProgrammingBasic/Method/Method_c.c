#include <stdio.h>

void HelloWorld(const char* name) {
    printf("Hello %s\n", name);
}

int main() {
    HelloWorld("Alice");
    return 0;
}
