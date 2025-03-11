#include <stdio.h>
#include <stdlib.h>

int main(void){
// malloc(), calloc(), realloc(),free()    

// 1- malloc()
    // int *ptr = (int *)malloc(sizeof(int) * 2);
    // if(ptr != NULL){
    //     ptr[0] = 10;
    //     ptr[1] = 20;
    //     printf("%d %d\n",ptr[0],ptr[1]);
    //     free(ptr);
    // }
    // else{
    //     print("no memory Allocation");
    // }
//2- calloc()
    // int *ptr = (int *)calloc(sizeof(int),10);
    // int *ptr2 = (int *)malloc(sizeof(int) * 10);
    // for(int i=0;i<10;i++){
    //     printf("%d %d\n",ptr[i],ptr2[i]);
    // }
    // free(ptr);
    // free(ptr2);

//3- realloc()
    // int key = 1,index = 0;
    // int capacitance = 2;
    // int *ptr = (int *)calloc(sizeof(int),capacitance);
    // printf("first pointer = %p\n",ptr);
    // while(1){
    //     printf("Enter Number or Exit if -1\n");
    //     scanf("%d",&key);
    //     if(key == -1)
    //         break;
    //     if(index == capacitance){
    //         // int *tmp = (int *)calloc(sizeof(int),(capacitance *= 2));
    //         // for(int i=0;i<index;i++)
    //         //     tmp[i] = ptr[i];
    //         // free(ptr);
    //         // ptr = tmp;
    //         ptr = (int *)realloc(ptr,sizeof(int) * (capacitance *= 2));
    //         printf("\n next Pointer %p\n",ptr);
    //     }
    //     ptr[index++] = key;
    // }
    // for(int i=0;i<index;i++){
    //     printf("%d ",ptr[i]);
    // }
    // printf("\n final Pointer %p\n",ptr);
    // free(ptr);
}