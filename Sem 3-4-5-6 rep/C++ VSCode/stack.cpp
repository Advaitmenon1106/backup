#include <iostream>
using namespace std;

int stack[100];
int top = -1;

int push(int val){
    top++;
    stack[top] = val;
}

int pop(){
    if (top == -1){
        cout << "Underflow";
    }
    else {
        top--;        
    }
}

int display(){
    for (int i = top; i>=0; i--){
        cout << stack[i] << endl;
    }
}

int main(){
    int insert, choice;
    do{
        cout << "Make a choice: ";
        cin >> choice;
        switch(choice){
            case 1: cout << "Enter an element: "; cin >> insert; push(insert); break;
            case 2: pop(); break;
            case 3: display(); break;
        }
    }while (choice <= 3);
}