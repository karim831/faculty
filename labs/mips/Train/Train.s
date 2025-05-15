## Comments

# Author:       Karem Osama
# Date:         15 May 2025
#Description    Training On Mips


## Assembler Directives

.data ## data stored in 32bit Ram

prompt: .asciiz "\n Please enter an integer: ";

result: .asciiz "\n The addition result = ";

.text
.globl main
## beq → PC-relative addressing(16bit) (Use Pc = PC + 4 + (offcet * 4)) => (Offcet = Specific Addresse - (PC + 4)) / 4 
## j → Pseudo-direct addressing(28bit real addresse and 4MSB from PC)

## Operating System Services : li ($v0), {
## some services: 
## 4  (Console Print String),
## 1  (Console print number),
## 5  (Console Read Input),
## 10 (exit program)}
## $a0 Register used in write , $v0 while Read uses
## $sp stack pointer for Full decreasing stack
## jal (jumb and addresse load) used when label function called and want to store next addresse(return addresse)
## $ra register where return addresse stored
## $at the assembler use to store temporary values while expanding the pseudo-instruction.
main:
li $v0 10;
syscall;



