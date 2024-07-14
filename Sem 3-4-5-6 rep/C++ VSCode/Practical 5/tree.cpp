#include <iostream>
using namespace std;
int head = NULL;

struct node {
    int data;
    struct node* left;
    struct node* right;
};

struct node* alloc(){
    new node;
}

struct node* preorder(){

}

struct node* inorder(){

}

struct node* postorder(){

}


int main(){
    int n, val;
    int temp;
    int data[n];
    cout << "Enter the number of values in your binary tree: ";
    cin >> n;
    for (int i = 0; i < n; i++){
        cout << "Enter element " << n << ": ";
        cin >> val;
        data[i] = val;
    }
    int preTemp;
    int root = data[0];
    temp = root;
    // 8  5  12  3  45  90  20

    for(int i = 0; i < n; i++){
        data[i] = preTemp;
        data [i+1] = temp;
        alloc();
        if (temp > preTemp){
            
        }
    }
    
}