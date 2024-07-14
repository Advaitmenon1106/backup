#include <iostream>
using namespace std;

int queue[5];
int n = 5;
int front = -1; 
int rear = -1; 

int isEmpty(){
    if (front == -1 && rear == -1){
        return 1;
    }
    else {
        return 0;
    }
}

int isFull(){
    if ((rear+1)%n == front){
        return 1;
    }
    else {
        return 0;
    }
}

int enqueue(int ins){
    if (isFull()){
        cout << "Queue is full.";        
    }
    else if (isEmpty()){
        front = 0;
        rear = 0;
    }
    else {
        rear = (rear +1)%n;
    }
    queue[rear] = ins;
}

int dequeue(){
    if (isEmpty()||front>rear){
        cout << "Queue is empty";
    }
    else if (front == rear){
        front = -1;
        rear = -1;
    }
    else {
        front = (front+1)%n;
    }
}

int display(){
    for (int i = front; i != rear; i = (i+1)%5){
        cout << queue[i] << endl;
    }
    cout << queue[rear] << endl;
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