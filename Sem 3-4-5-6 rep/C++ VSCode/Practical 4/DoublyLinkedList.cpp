#include <iostream>
using namespace std;

struct node{
    int data;
    struct node*next;
    struct node*prev;
};

struct node* head = NULL;

struct node* insertFromBeg(int beg){
    struct node* newnode = new node;
    cout << "Enter a value: ";
    cin >> beg;
    if (head == NULL){
        newnode->prev = NULL;
        newnode->data = beg;
        newnode->next = NULL;
        head = newnode;
    }
    else {
        newnode->data = beg;
        newnode->prev = NULL;
        newnode->next = head;
        head = newnode;
    }
}

struct node* insertFromEnd(int end){
    cout << "Enter a value: ";
    cin >> end;
    node* counter = head;
    struct node* newEndnode = new node;
    if(head == NULL){
        newEndnode->data = end;
        newEndnode->prev = NULL;
        newEndnode->next = NULL;
        head = newEndnode;
    }
    else {
        while (counter->next != NULL){
            counter = counter->next;
        }
        counter->next = newEndnode;
        newEndnode->data = end;
        newEndnode->prev = counter;
        newEndnode->next = NULL;
    }
}

struct node* deleteFromBeg(){
    struct node * pointer = head;
    if (head == NULL){
        cout << "Underflow";
    }
   if (head->next == NULL){
        head == NULL; 
        delete pointer;
    }
    head = head ->next;
    head->prev = NULL;
    delete pointer;
}

struct node* deleteFromEnd(){
    struct node* ptr = head;
    struct node* preptr = head;
    if (head == NULL){
        cout << "Underflow";
    }
    while (ptr->next != NULL){
        ptr = ptr->next;
    }
    preptr = ptr->prev;
    preptr->next = NULL;
    delete ptr;    
}

void delFromAnyPosition(int pos){
    int counter = 0;
    struct node* del = head;
    struct node*preptr;
    struct node* postptr;
    while (counter!= pos){
        del = del->next;
        counter++;
    }
    del = del->next;
    postptr = del->next;
    preptr = del->prev;
    preptr->next = postptr;
    postptr->next = preptr;
    delete del;

}

struct node* display(){
    node* traverse;
    traverse = head;
    if (head == NULL){
        cout << "Empty";
    }    
    else {
        while(traverse != NULL){
            cout << traverse->data << " " << endl;
            traverse = traverse->next;
        }
    }
}

int main(){
    int choice, insBeg, insEnd, position;
    do {
        cout << "Make a choice: ";
        cin >> choice;
        switch(choice){
            case 1: insertFromBeg(insBeg); break;
            case 2: insertFromEnd(insEnd); break;
            case 3: deleteFromBeg(); break;
            case 4: deleteFromEnd();break;
            case 5: cout << "Enter the position from which you need to delete the element: ";
            cin >> position;
            delFromAnyPosition(position);break;
            case 6: display(); break;
        } 
    } while (choice<=6);
}