#include <iostream>
using namespace std;
int n = 14;
int array[14];
int array[] = {1,2,3,4};
int avg, sumOfsquares;


int mean(){
    int sum = 0;
    for (int i = 0; i<n; i++){
        sum = sum + array[i];
    }

    int average = sum/n;
    cout << average << endl;

    avg = average;
}

int median(){
    int temp;
    for(int i=0;i<n;i++)
	{		
		for(int j=i+1;j<n;j++)
		{
			if(array[i]>array[j])
			{
				temp =array[i];
				array[i]=array[j];
				array[j]=temp;
			}
		}
	}
     for(int k = 0; k<n; k++){
            cout << array[k] << " " << endl ;
        }
        int add = array[7]+array[8];
        int median = add/2;
        cout << "Median = " << median << endl;
}

int probability(int E){
    int counter = 0;
    for (int i = 0; i<n; i++){
        if(E == array[i]){
            counter++;
        }
    }
    cout << counter << endl;
    cout << "Probability: " << counter/14;
}

int avgOfSquares(){
    float sumOfsq=0;
    int temp;
    for (int i = 0; i<n ; i++){
        temp = array[i]*array[i];
        sumOfsq = sumOfsq+temp;
    }
    cout << "Sum of squares: " << sumOfsq << endl;
    cout << "Average of squares: " << sumOfsq/14 << endl;

    sumOfsquares = sumOfsq/14;
}

int stdDeviation(){
    float avgSq = avg*avg;
    float difference = sumOfsquares- avgSq; 
    float deviation = sqrt(difference);
    cout << deviation;
}


int main(){
    int choice, elements, event;
    for (int i = 0; i<n; i++){
        cout << "Enter element " << i+1 << " : ";
        cin >> array[i];
    }
    do{
        cout << "Make a choice: ";
        cin >> choice;
        switch(choice){
            case 1: cout << "Enter a value: "; cin >> event;             
            probability(event);break;
            case 2: mean(); break;
            case 3: median(); break;
            case 4: avgOfSquares(); break;
            case 5: stdDeviation(); break;
        }
    }while (choice <= 5);
}