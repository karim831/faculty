#include <stdio.h>
#include <stdlib.h>
FILE *ptr;
int main(void){
    // fopen(),fprintf(),fgets(),fclose()
    // ptr = fopen("Document.txt","w");
    ptr = fopen("Document.txt","r");
    if(ptr != NULL){
        // fprintf(ptr,"User Id = %d,Name = %s, Age = %d",1,"karim",21);
        // fclose(ptr);

        // ptr = fopen("Document.txt","r");
        // char data[100];

        // fgets(data,100,ptr);
        // printf("%s\n",data);
        char data[100];
        while(fgets(data,100,ptr)){
            printf("%s",data);
        }
    }
    else{
        printf("Error while Opening File");
    }
}