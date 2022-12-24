#include<iostream>
#include<cstdlib>
#include<time.h>

using namespace std;


int main(){
    int size;

    cout << "Enter size of grid: " ;
    cin >> size;
    cout << endl;

    int grid[size][size], counter1 = 0, counter2 = 0, xcords[size], ycords[size], x, y;
    char field[size][size];
    bool check;
    

    // Initializes the grid and field
    while(counter1 < size){
        counter2 = 0;
        while(counter2 < size){
            field[counter1][counter2] = 'x';
            grid[counter1][counter2] = 0;
            counter2++;
        }
        counter1++;
    }

    counter1 = 0, counter2 = 0;


    // Adds mines and checks there are no duplicates
    srand(time(0));
    while(counter1 < size){
        check = false;
        counter2 = 0;
        x = rand()%size;
        y = rand()%size;
        while(counter2 < size){
            if(xcords[counter2] == x && ycords[counter2] == y){
                check = true;
            }
            counter2++;
        }
        if(check){
            continue;
        }
        xcords[counter1] = x;
        ycords[counter1] = y;
        grid[x][y] = 1;
        counter1++;

    }

    counter1 = 0, counter2 = 0;
    while(counter1<size){
            counter2 = 0; 
            while(counter2 < size){
                cout << grid[counter1][counter2] << " ";
                counter2++;
            }
            cout << endl;
            counter1++;
    }
    
}
