#include<iostream>
#include<time.h>

using namespace std;

int SIDE;

void placeMines(int grid[][50], char field[][50], int mines[][2]){

    srand(time (NULL));

	for (int i=0; i<SIDE; i++){
		for (int j=0; j<SIDE; j++){
			grid[i][j] = 0;
            field[i][j] = 'x';
		}
	}

    for(int i = 0; i<SIDE;){
        int x = rand()%SIDE;
        int y = rand()%SIDE;
        if(grid[x][y]){
            continue;
        }
        mines[i][0] = x;
        mines[i][1] = y;
        grid[x][y] = 1;
        i++;
    }
}

void showField(char field[][50]){
    for(int i = 0; i < SIDE; i++){
        for(int j = 0; j < SIDE; j++){
            cout << field[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){

    bool game = true;
    int grid[50][50], mines[50][2], x, y;
    char field[50][50];

    cout << "Enter the number of sides(cannot be more than 99): ";
    cin >> SIDE;

    placeMines(grid, field, mines);
    
    for(int i = 0; i < SIDE; i++){
        for(int j = 0; j < SIDE; j++){
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    while(game){
        showField(field);
        cout << "Enter the X value: ";
        cin >> x;
        cout << "Enter the Y value: ";
        cin >> y;


    }

}
