#include<iostream> 
#include<queue> 
#include<stack> 
using namespace std; 
int adj[3][3] = {{1,0,1}, {0,1,0}, {0,0,1}};
int visited[9];


void bfs(int source, int n){
    queue<int>q;
    for(int i=0;i<n;i++){
        visited[i] = 0;
    }

    q.push(source);
    visited[source]=1;
    while(!q.empty()) {

        source=q.front(); 
        cout<<source;
        q.pop(); 

        for(int k=0;k<n;k++){ 
            if(adj[source][k]==1){

                if(visited[k]==0){
                    visited[k]=1; 

                    q.push(k);
                }
            }
        }
    }
}


void dfs(int source, int n){
   stack<int>s; 
   s.push(source); 
   visited[source]=1; 
   while(!s.empty()){
       source=s.top(); 
       cout<<source;
       s.pop();
       for(int k=0;k<n;k++){
           if(adj[source][k]==1 && visited[k]==0){
                visited[k]=1; 
                s.push(k); 

            }
       } 

   } 
} 

int main(){

    int x,sour; 
    cout<<"Enter no. of vertices: "<<endl; 
    cin>>x;
    cout<<"Enter source vertex: "<<endl; 

    cin>>sour; 

    int choice; 

    do{
        cout<< " Make a choice: ";
        cin>>choice;  

        switch(choice){
            case 1: bfs(sour,x); break;
            case 2: dfs(sour,x);break;
        }
    } while (choice <= 2);
}