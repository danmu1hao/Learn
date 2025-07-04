#include <iostream>
using namespace std; // std名前空間を省略するため

int main() {
    string name; 
    // std::cout << "std付けてもいい "; 
    //<< >>插入演算子 endl 改行
    cout << "Please enter your name:"; 
    cin >> name; 
    cout << "hello " << name << endl; 
    return 0;
} 