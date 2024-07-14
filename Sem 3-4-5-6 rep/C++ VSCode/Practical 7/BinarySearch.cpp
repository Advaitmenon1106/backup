#include <iostream>
using namespace std;

int array[7];
int size = 7;
int mid = 4;


int selectionSort(int a[], int n){
    for (int i = 0; i<n-1; i++){
        int min = i;
        for (int j = 1; j<n; j++){
            if (a[j] < a[min]){
                min = j;
            }
        }
        int temp;
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }
}

int binarySearch(int arr[], int low, int high){
    int num;
    cout << "Enter element to be searched: ";
    cin >> num;
    low = array[0];
    high = array[6];
    while (low<= high){
        int middle = (low + high)/2;
        if (array[middle] < num){
            low = mid+1;
        }
        else if (array[middle] == num){
            return middle;
        }
        else if (array[mid] > num){
            high = mid-1;
        }
    }
}

int main(){
    for (int i = 0; i<7; i++){
        cout << "Enter element " << i+1 << ": ";
        cin >> array[i];
    }
    int lowerBound = array[0];
    int upperBound = array[6];

    selectionSort(array, size);
    int searched = binarySearch(array, lowerBound, upperBound);
    cout << searched+1;
}