#include <iostream>
#include <queue>
using namespace std;

int source = 0;
queue<int> visited;
int n=3;
int adjMatrix[3][3] = {{0,1,0}, {1,0,1}, {0,1,0}};

int bfs(){
    visited.push(adjMatrix[0][0]);
    while(!visited.empty()){
                
    }
}
int main(){
    for (int i = 0; i<n; i++){
        for (int j = 0; j<n; j++){
            cout << adjMatrix[i][j] << " ";
        }
        cout << endl;
        
    }

}