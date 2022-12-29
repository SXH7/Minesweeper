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

bool sanityCheck(int x, int y){
    if(x > 0 && y > 0 && x < SIDE && y < SIDE){
        return true;
    }
    else{ 
        return false;
    }
}

int countMines(int grid[][50], int x, int y){
    int count = 0;

    if(sanityCheck(x-1, y+1) && grid[x-1][y+1]){
        count++;
    }
    if(sanityCheck(x, y+1) && grid[x][y+1]){
        count++;
    }
    if(sanityCheck(x+1, y+1) && grid[x+1][y+1]){
        count++;
    }
    if(sanityCheck(x-1, y-1) && grid[x-1][y-1]){
        count++;
    }
    if(sanityCheck(x, y-1) && grid[x][y-1]){
        count++;
    }
    if(sanityCheck(x+1, y-1) && grid[x+1][y-1]){
        count++;
    }
    if(sanityCheck(x-1, y) && grid[x-1][y]){
        count++;
    }
    if(sanityCheck(x+1, y) && grid[x+1][y]){
        count++;
    }

    return count;
    
}

bool reveal(int x, int y, char field[][50], int grid[][50]){

    if(field[x][y] != 'x'){
        return false;
    }

    if(grid[x][y]){
        cout << "You Lost :<";
        return false;
    }
    else{
        int count = countMines(grid, x, y);
        field[x][y] = count + '0';

        if(!count){
            if(sanityCheck(x-1, y) && !grid[x-1][y]){
                reveal(x-1, y, field, grid);
            }
            if(sanityCheck(x+1, y) && !grid[x+1][y]){
                reveal(x+1, y, field, grid);
            }
            if(sanityCheck(x-1, y-1 && !grid[x-1][y-1])){
                reveal(x-1, y-1, field, grid);
            }
            if(sanityCheck(x, y-1) && !grid[x][y-1]){
                reveal(x, y-1, field, grid);
            }
            if(sanityCheck(x+1, y-1) && !grid[x+1][y-1]){
                reveal(x+1, y-1, field, grid);
            }

            if(sanityCheck(x-1, y+1) && !grid[x-1][y+1]){
                reveal(x-1, y+1, field, grid);
            }
            if(sanityCheck(x, y+1) && !grid[x][y+1]){
                reveal(x, y+1, field, grid);
            }
            if(sanityCheck(x+1, y+1) && !grid[x+1][y+1]){
                reveal(x+1, y+1, field, grid);
            }
        }
    
        return true;

    }

}

bool win(char field[][50], int grid[][50]){
    int unrevealed = 0;
    for(int i = 0; i < SIDE; i++){
        for(int j = 0; j < SIDE; j++){
            if(!grid[i][j] && field[i][j]){
                return false;
            }
        }
    }
    return true;
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

        game = reveal(x, y, field, grid);

        if(win(field, grid)){
            cout << "You Win!";
            break;
        }

    }

}
