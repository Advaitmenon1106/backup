#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(){
    srand(time(0));
    int number = rand()%100;
    int counter = 0;
    int guess;
    while (counter <=8){
        cout << "Enter a guess between 0 and 100: ";
        cin >> guess;
        counter ++;
        if (guess < number){
            cout << "Your number is lesser than the number to be guessed. Try again." << endl;
        }
        else if (guess > number){
            cout << "Your number is greater than the number to be guessed. Try again." << endl;
        }
        else if (guess == number){
            cout << "Correct.";
            break;
        }
    }
} 