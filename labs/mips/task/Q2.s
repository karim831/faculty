.data 
    array: .word 0:30 ;
    input_msg: .asciiz "Enter the 30 integers or exit with negative\n";
    output_ms: .asciiz "Number Of Odds : ";
.text
.globl main

main: 
    li $v0, 4;
    la $a0, input_msg;
    syscall;
   
    li $t0, 0;
    li $s0, 0;
loop:    
    li $v0, 5;
    syscall;
    blt $v0, 0, count_odd; 
    sw $v0, array($t0); 
    addi $t0, 4;
    beq $t0, 120, count_odd;
    j loop;    


count_odd:
    beq $t0, 0, end;
    addi $t0, -4;
    lw $s1, array($t0);
    and $s1, 1;
    beq $s1, 0, count_odd;
    addi $s0, 1;
    j count_odd;
    
end:
    la $a0, output_ms; 
    li $v0, 4; 
    syscall;

    li $v0, 1; 
    move $a0, $s0;
    syscall;
    li $v0, 10;
    syscall;

