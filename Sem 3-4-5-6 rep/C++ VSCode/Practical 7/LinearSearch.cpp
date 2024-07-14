#include <iostream>
using namespace std;
int array[10];
int n = 10;
int pos;

int containsElement(int k){
    for (int i = 0; i<n; i++){
        if (array[i] == k){
            cout << "Element present in array at position " << i+1;
        }
    }
}

int main(){
    for (int i = 0; i<n; i++){
        cout << "Enter element " << i+1 << ": ";
        cin >> array[i];
    }
    for (int i = 0; i<n; i++){
        cout << array[i] << " " ;
    }
    int element;
    cout << "Enter an element: ";
    cin >> element;
    containsElement(element);
    }