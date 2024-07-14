#include <iostream>
using namespace std;

int stack[10];
int top = -1;

int push(int val){
    if (top == 10){
        cout << "Overflow." << endl;
    }
    else {
        top++;
        stack[top] = val;
    }
}

int pop(){
    if (top == -1){
        cout << "Underflow.";
    }
    else {
        top--;
    }
}

int display(){
    if (top == -1){
        cout << "No elements in stack.";
    }
    else{
        for (int i = top; i>=0; i--){
        cout << stack[i] << endl;
        }
    }
}

int peep(int pos){
    cout << stack[pos-1];
}

int main(){
    int choice, ins, position;
    do {
        cout << "Make a choice {1- Pushes element into stack; 2- pops element; 3- displays elements in stack; 4- shows element at a position}: ";
        cin >> choice;

        switch (choice){
            case 1: cout << "Insert an element you want to push into the stack: ";
            cin >> ins;
            push(ins);
            break;

            case 2: pop();
            break;

            case 3: display();
            break;

            case 4: cout << "Enter the position: "; cin >> position; peep(position); break;

            default: "Invalid choice, program terminated.";
        }
    } while (choice <= 4);
}

