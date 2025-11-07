// include and define section 
#include <avr/io.h>
#include <avr/interrupt.h>
#define F_CPU 8000000UL
#define P_Scaler 1024
#define CS ((1 << CS12) | (1 << CS10)) 
#define on_off_time 2
#define OCR ((on_off_time * (F_CPU * 1.0 / P_Scaler)) - 1)



void pin_init(){
    DDRB |= 1 << DDB0;
    PORTB |= 1 << PORTB0;
}


void time_init(){
    TCCR1B = 0;
    TCCR1A = 0;
    TCNT1 = 0;
    OCR1A = OCR;

    TIMSK |= 1 << OCIE1A;
    TCCR1B |= (1 << WGM12) | CS;
    sei();
}

int main(){
    pin_init();
    time_init();
    while(1){}
}

ISR(TIMER1_COMPA_vect){
    PORTB ^= (1 << PORTB0);
}