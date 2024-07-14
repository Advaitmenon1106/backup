#include <iostream>
using namespace std;

int main (){
    int array[10];
    int k;
    for (int i = 0; i<10; i++){
        cout << "Enter element " << i+1 << ": ";
        cin >> array[i];
    }

    cout << "Enter an element: ";
    cin >> k;
    for (int j = 0; j<10; j++){
        if (array[j] == k){
            cout << "Element exists in the array";
            break;
        }
    }
}