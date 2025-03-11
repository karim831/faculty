#include <stdio.h>
#include "matrix_ops.h"

void sum(int n, int m, int matrix1[n][m], int matrix2[n][m]){
    for(int i=0;i<n;i++){ // i = 0,1,...n 
        for(int j=0;j<m;j++){ // j =0, 1, 2, 3,4 , m
            printf("%d ",matrix1[i][j] + matrix2[i][j]);
        }
        printf("\n");
    }
}


void diff(int n, int m, int matrix1[n][m], int matrix2[n][m]){
    for(int i=0;i<n;i++){ // i = 0,1,...n 
        for(int j=0;j<m;j++){ // j =0, 1, 2, 3,4 , m
            printf("%d ",matrix1[i][j] - matrix2[i][j]);
        }
        printf("\n");
    }
}


void mul(int n, int m, int w, int matrix1[n][m], int matrix2[m][w]){
    for(int i=0;i<n;i++){
        for(int j=0;j<w;j++){
            int sum = 0;
            for(int k=0;k<m;k++){
                sum += matrix1[i][k] * matrix2[k][j];
            }
            printf("%d ", sum);
        }
        printf("\n");
    }
}