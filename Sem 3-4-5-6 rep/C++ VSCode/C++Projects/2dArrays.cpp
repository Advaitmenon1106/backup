#include <iostream>
#include <string.h>
using namespace std;

struct attendance{
    string name[100];
    char week1;
    char week2;
};

int main(){
    attendance details;
    int choice;
    do{
        switch(choice){
            case 1: cout << "Name: ";
            getline(cin, details.name);
            cout << "Attendance in week 1: ";
            cin >> details.week1;
        }
    } while (true);
}