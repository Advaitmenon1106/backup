#include <iostream>
using namespace std;

int fib(int n){
    if (n <= 1){
        return n;
    }
    else {
         return fib(n-1)+fib(n-2);
    }
}

int main(){
    int num;
    cout << "Enter a number: ";
    cin >> num;
    int k = fib(num);
    for (int i = 0; i<k ; i++){
        cout << fib(i);
    }
}