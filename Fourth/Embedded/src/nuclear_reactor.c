#include<avr/io.h>
#include<avr/interrupt.h>
#include<math.h>
#define F_CPU 4000000UL
#define OCR 10
#define P_SCALER 1024
#define CS0 ((1 << CS02) | (1 << CS01) | (1 << CS00))
#define CS1 ((1 << CS12) | (1 << CS10))


void pins_init(){
    DDRB &= ~(1 << DD0);
    DDRC = 0xFF;
    PORTC = 0;
}


void timer0_init(){
    TCCR0 = 0;
    TCNT0 = 0;
    OCR0 = OCR;

    TIMSK |= (1 << OCIE0);
    TCCR0 |= (1 << WGM01) | (CS0);
    sei();
}

void timer1_init(){
    TCCR1A = 0;
    TCCR1B = 0;
    TCNT1 = 0;

    TCCR1B |= CS1;
}



int main(){
    pins_init();
    timer0_init();
    timer1_init();    

    while(1){}
}


ISR(TIMER0_COMP_vect){
    // PORTC = (TCNT1 + 1) * (P_SCALER / F_CPU);
    PORTC = round((TCNT1 + 1) * (P_SCALER * 1.0 / F_CPU));
    TCNT0 = 0;
    TCNT1 = 0;
}






