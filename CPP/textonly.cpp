#include<iostream>
#include<cstring>


using namespace std;

void addmines(int side, char grid[][8], char field[][8]){
    int counter1 = 0;
    while(counter1<side){
        int counter2 = 0;
        while(counter2 < side){
            field[counter1][counter2] = 'x';
            counter2++;
        }
        counter1++;
    }
}

int main(){

    int side = 8;
    char x, grid[8][8], field[8][8];

    /* cout << "Enter the difficulty. E for Easy, M for medium, H for hard. \n";
    cin >> x;
    x = toupper(x);

    if(x == 'E'){
        side = 8;
    }
    else if(x == 'M'){
        side = 10;
    }
    else if(x == 'H'){
        side = 12;
    } */

    addmines(side, grid, field);

    return 0;
}
