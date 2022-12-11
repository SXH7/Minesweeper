#include<iostream>
#include<cstring>

using namespace std;

void gridgen(int side){
    cout <<"test";
}

int main(){

    int side;
    char x;

    cout << "Enter the difficulty. E for Easy, M for medium, H for hard. \n";
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
    }

    gridgen(side);

    return 0;
}
