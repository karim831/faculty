#include <stdio.h>
#include "matrix_ops.h"


int main(void){
    int n,m;
    scanf("%d%d",&n,&m);

    int matrix1[n][m],matrix2[n][m];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&(matrix1[i][j]));
        }
    }

    printf("\n");

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&(matrix2[i][j]));
        }
    }

    sum(n,m,matrix1,matrix2);
    printf("\n");
    diff(n,m,matrix1, matrix2);
    printf("\n");
    mul(n,m,n,matrix1,matrix2);
}


