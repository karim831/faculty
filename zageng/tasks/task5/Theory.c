/* Difference between Swapping two values by Reference and by value : Explained in code*/
/* Pointer Types : 
        1-DataType Pointers: void, char, short, int, long long, float, double
        2-Wild Pointer : uninitiallized pointer can reference to random addresses(dangerous)
        3-NULL Pointer : pointer To No Addresse
        4-dungle Pointer : freed pointer the pointer may point to the specific addresse but
            this addresse became out scope of the program 
        5-pointer to pointer : a pointer points to another pointer like pointer to array
        6-pointer to function 
*/

int x; // uninitlized global variable => bss
int y = 23; //initialized global variable => data
const int z = 5; // initialized constant global variable => rodata in data  

int main(void){
    int var1 = 2;  //local variable => stack
    const int var2 = 3; //constant local variable => stack but using optimizing can be in rodata
}