#include<iostream>
#include<cstring>

using namespace std;

int gridgen(int side){
    int counter = 0, counter2 = 0;
    char arr[8];
    while(counter < side){
        while(counter2 < side){
            arr[counter2] = 'e';
            counter2++;
        }
        counter++;
    }

    return arr[8];
}

int main(){
    
    int side = 8;
    char arr[8] = gridgen(side);
    


    return 0;
}
