#include <iostream>
using namespace std;

int queue[500];
int n = 500;
int front = -1;
int rear = -1;



int enqueue(int ins){
    if (rear == n-1){
        cout << "Queue overflow";
    }

    else { 
        if (front = -1){
        front = 0;
        rear++;
        queue[rear] = ins;
        }
    }
}

int dequeue(){
    if (front == -1 || front > rear){
        cout << "Queue Underflow";
    }
    else {
        front ++;
        cout << queue[front] <<  " is the element that is deleted from the queue.";
    }
}

int display(){
    if (front = -1){
        cout << "Queue is empty";
    }
    else {
        for (int i = front; i <= rear; i++){
            cout << queue[i] << endl;
        }
    }
}

int main(){
    int choice;
    int insertedElement;
    do{
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