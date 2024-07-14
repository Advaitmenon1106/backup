#include <iostream>
using namespace std;

int queue[1000];
int n = 1000;
int front = -1; //element is deleted from the front
int rear = -1; //element is added from the rear
//   { 1  3  5  7  9  11 } element deleted = 1, element added : after 11
//-1 { 0  1  2  3  4  5  } front = index no. 0; rear = index no. 5 (in given array)

int enqueue(int ins){

    if (rear == n-1){
        cout << "Queue overflow";
    }

    else{

        if (front == -1){
        front = 0;
    }
    rear++;
    queue[rear] = ins;
    }
}

int dequeue(){
    if (front == -1 && rear == -1){
        cout << "Queue is empty" << endl;
    }
    else {
        front++;
    }
}

int display(){
    if (front == -1 || front > rear){
        cout << "Queue is empty" << endl;
    }
    else {
        for (int i = front ; i <= rear; i++){
            cout << queue[i] << endl;
        }
    }
}

int main() {
    int choice, insertedElement;
    do {
        cout << "Make your choice ( {1} Insert an element; {2} delete an element; {3} display the queue ): ";
        cin >> choice;
        switch (choice){
            case 1 : cout << "Enter any element to be added to the queue: ";
            cin >> insertedElement;
            enqueue(insertedElement); break;

            case 2 : dequeue(); break;

            case 3 : display(); break;

            default : cout << "Invalid option, try again.";
        }
    }while (choice <= 3); 
    
}