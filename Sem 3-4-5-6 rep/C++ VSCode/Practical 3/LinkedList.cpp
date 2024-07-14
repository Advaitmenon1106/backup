#include <iostream>
using namespace std;

struct node {
    int data;
    struct node* next;
};

struct node* head = NULL;

struct node* modify(int oldVal, int newVal){
    struct node* pointer = head;
    while (pointer->data!=oldVal){
        pointer = pointer->next;
    }
    pointer->data = newVal;
}

struct node* insert_beg(int insertBeg){
    struct node* newnode = new node;
    newnode->data = insertBeg;
    newnode->next = head;
    head = newnode;
}

struct node* insert_end(int insertEnd){
    node* newnode = new node;
    node* counter;
    if (head == NULL){
        struct node* newnode = new node;
        newnode->data = insertEnd;
        newnode->next = head;
        head = newnode;        
    }
    else{
        counter = head;
        newnode->data = insertEnd;
        newnode->next = NULL;
        while(counter->next != NULL){
            counter = counter->next;
    }
        counter->next = newnode;
    }
}

struct node* del_beg(){
    node* current;
    if (head == NULL){
        cout << "Underflow";
    }
    current = head;  
    head = head->next;
    delete current;  
}
struct node* del_end(){
    if (head == NULL){
        cout << "Underflow";
    }
    node* ptr = head;
    node* preptr = ptr;
    while (ptr->next != NULL){
        preptr = ptr;
        ptr = ptr->next;
    }
    preptr->next = NULL;
    delete ptr;
}

struct node* display(){
    int counterVar = 0;
    if (head == NULL){
        cout << "Underflow";
    }
    node* count = head;
    while (count!= NULL){

        cout << count->data << " " << endl;
        count = count->next;
        counterVar++;
    }
    cout << endl;
    cout << counterVar << " elements in list.";
}

int main(){
    int choice, insert_at_beg, insert_at_end, oldData, newData;
    do{
        cout << "Make a choice: ";
        cin >> choice;
        switch(choice){
            case 1: cout << "Enter the element to be added: "; cin >> insert_at_beg; insert_beg(insert_at_beg); break;
            case 2: cout << "Enter the element to be added: "; cin >> insert_at_end; insert_end(insert_at_end); break;
            case 3: del_beg(); break;
            case 4: del_end(); break;
            case 5: display(); break;
            case 6: cout << "Enter a data to be replaced: ";
            cin >> oldData;
            cout << "Enter the new data: ";
            cin >> newData;
            modify(oldData, newData); break;
            default : "Invalid"; break;
        }
    }
    while (choice <= 6);
}