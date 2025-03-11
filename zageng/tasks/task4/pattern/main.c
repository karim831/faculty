#include <stdio.h>

void RightHalfPyramid(int num){
    for(int i=0;i<num;i++){ // 5 => 0,1,2,3,4
        for(int j=0;j<=i;j++) printf("*");
        printf("\n");
    }
}
// num-1, num-2, num-3

void Pyramid(int num){
    int counter = 1;
    for(int i = 0;i < num;i++){ 
        for(int j=i+1;j<num;j++) printf(" ");
        for(int j=0;j<counter;j++) printf("*");
        printf("\n");
        counter+=2; 
    }
}

void InvertedPyramid(int num){
    int start = 1 + 2 * (num-1);
    int counter = 0;
    for(int i=0;i<num;i++){
        for(int j=0;j<counter;j++) printf(" ");
        for(int j=0;j<start;j++) printf("*");
        start-=2;
        counter++;
        printf("\n");
    }
}

void main(void){
    RightHalfPyramid(5);
    printf("\n");
    Pyramid(5);
    printf("\n");
    InvertedPyramid(5);
}