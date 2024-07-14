#include <iostream>
using namespace std;

int main(){
    int x, y;
    int *ptr;
    x = 10;
    ptr = &x;
    y = *ptr;
    cout << x << " " << &x << endl;
    cout << *&x << " " << &x << endl;
    cout << *ptr << " " << ptr << endl;
    cout << y << " " << &*ptr << endl;
    cout << ptr << " " << &ptr << endl;
    cout << y << " " << &y << endl;
    *ptr = 25; 
    cout << x << endl;
}