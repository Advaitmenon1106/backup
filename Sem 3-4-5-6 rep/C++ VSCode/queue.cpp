#include <iostream>
using namespace std;

int cqueue[10];
int front = -1;
int rear = -1;
int max = 10;

int isFull(){
    if ((rear+1)%max == front){
        return 1;
    }
    else {
        return 0;
    }
}

int isEmpty(){

}

int enqueue(){
    
}

int dequeue(){

}

