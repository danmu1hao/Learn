#include <iostream>
using namespace std;

void HelloWorld(const string& name) {
    cout << "Hello " << name << endl;
}

int main() {
    HelloWorld("Alice");
    return 0;
}
