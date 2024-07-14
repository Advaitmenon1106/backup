#include <iostream>
#include <string>
using namespace std;
char stack[100];
int top = -1;

void push(char element){
    if (top == 100){
        cout << "Overflow";
    }
    else{
    top++;
    stack[top] = element;
    }
}

void pop (){
    if (top == -1){
        cout << "Underflow" << endl;
    }
    else {
        top--;
    }
}

int main(){
    string expression;
    char c;
    int len = expression.length();
    cout << "Enter an expression: ";
    getline(cin, expression);
    for (int i = 0; i < len; i++){
        c = expression.at(i);
        if (c == '[' || c == '{' || c == '('){
            push(c);
        }
        else if (c == ']' && stack[top] == '['){
            pop();
        }
        else if (c == '}' && stack[top] == '{'){
            pop();
        }
        else if (c == ')' && stack[top] == '('){
            pop();
        }
    }
    if (top==-1){
        
        cout << "Balanced." << endl;
    }
    else {
        cout << "Unbalanced." << endl;
    }

}