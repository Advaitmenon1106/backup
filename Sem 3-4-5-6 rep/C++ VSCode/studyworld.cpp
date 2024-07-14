#include <iostream>
using namespace std;

int main(){
    int n;
    int arr[n];
    cout << "Enter number of elements: ";
    cin >> n;
    for (int i = 0; i<n; i++){
        cout << "Enter element: ";
        cin >> arr[i];
    }
    for (int j = 0; j<n; j++){
        for (int k = n-1; k>=0; k--){
            arr[j] = arr[k];
        }
    }
    for (int m = 0; m<n; m++){
        cout << arr[m] << " ";
    }       
}
