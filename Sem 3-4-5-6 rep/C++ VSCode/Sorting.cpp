#include<iostream>
using namespace std;

int array[8];
int size = 8;

void insertionSort(int a[], int n){
    for (int i = 0; i<n; i++){
        int val = a[i];
        int hole = i;
        while (hole>0 && a[hole-1] > val){
            a[hole] = a[hole-1];
            hole = hole-1;
        }
        a[hole] = val;
    }
}

int selectionSort(int arr[], int n){
    for (int i = 0; i<n-1; i++){
        int min = i;
        for (int j = 1; j<n; j++){
            if (arr[j] < arr[min]){
                min = j;
            }
        }
        int temp;
        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

void display(int intArray[], int cap){
     for (int j = 0; j<cap; j++){
        cout << intArray[j] << " ";
    }    
}

int main(){
    int choice; 

    for (int i = 0; i<size; i++){
        cout << "Enter element " << i+1 << ": ";
        cin >> array[i];
    }


    do{
        cout << "Make a choice: ";
        cin>> choice;

        switch(choice){
            case 1: selectionSort(array, size); display(array, size); break;
            case 2: insertionSort(array, size); display(array, size); break;
        }
    } while (choice <= 2);
}