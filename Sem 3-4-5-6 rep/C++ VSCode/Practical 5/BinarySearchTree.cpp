#include <iostream>
using namespace std;

int count(int n){
    n = n+1;
    return n;
}

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* insert(struct node*root, int val){
    node* newnode = new node;
    newnode->data = val;
    newnode->right = NULL;
    newnode->left = NULL;
    if (root == NULL){
        root = newnode;
    }
    else if (val < root->data){
        root->left = insert(root->left, val);    
    }
    else if (val>root->data){
        root->right = insert(root->right, val);
    }
    return root;
}

struct node * inorderDisplay(struct node* root){
    if (root != NULL){
        inorderDisplay(root->left);
        cout << root->data << ", " << endl;
        inorderDisplay(root->right);
    }
    return root;
}

struct node* preorderDisplay(struct node* root){
    if (root != NULL){
        cout << root->data << " " << endl;
        preorderDisplay(root->left);
        preorderDisplay(root->right);
    }
    return root;
}

struct node* postorderDisplay(struct node* root){
    
    if (root != NULL){
        
        preorderDisplay(root->left);
        preorderDisplay(root->right);
        cout << root->data << " " << endl;
        
    }
    return root;
}

int main(){
    int ins, choice;
    struct node* root = NULL;
    do{
        cout << "Make a choice: ";
        cin >> choice;
        switch (choice){

            case 1: cout << "Enter a value: ";
                    cin >> ins;
                    root=insert(root, ins);
                    break;

            case 2: inorderDisplay(root);
            break;

            case 3: preorderDisplay(root);
            break; 

            case 4: postorderDisplay(root);
            break;                   
                    
        }
    } while (choice <= 4);
}