#include <iostream>
using namespace std;

int factorial(int num){
    
    if (num == 0 || num == 1){
        return 1;
    }
    else if (num > 1){
        return num * factorial (num-1);
    }

    return 0;
}


int main (){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int g = factorial(n-1) ;
    cout << g;
}