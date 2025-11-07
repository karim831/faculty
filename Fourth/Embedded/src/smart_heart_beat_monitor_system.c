#include<avr/io.h>
#include<avr/interrupt.h>
#include<math.h>

#define F_CPU 8000000

#define P_SCALAR1 1024
#define TIC_TIME1 ((P_SCALAR1 * 1.0) / F_CPU)
#define TOTAL_OV1 (TIC_TIME1 * 65536) 
#define TCCR1B_SETUP ((1 << CS12) | (1 << CS10))
#define TIMSK_TIMER1_SETUP (1 << TOIE1)
 
#define TCCR0_SETUP ((1 << CS02) | (1 << CS01) | (1 << CS00))


#define BLUE_LED PC0
#define GREEN_LED PC1
#define RED_LED PC2
#define HEART_SENSOR PB0

uint8_t BPM = 0;

void timer1_BPM_measurement_init(){
    TCCR1B = 0;
    TCNT1 = 0;

    TIMSK |= TIMSK_TIMER1_SETUP;
    TCCR1B |= TCCR1B_SETUP;
}

void timer0_heart_pulse_tracker_init(){
    TCCR0 = 0;
    TCNT0 = 0;

    TCCR0 |= TCCR0_SETUP;
}

void timers_init(){
    timer0_heart_pulse_tracker_init();
    timer1_BPM_measurement_init();
    sei();
}

void pin_init(){
    DDRC |= (1 << BLUE_LED) | (1 << GREEN_LED) | (1 << RED_LED);
    PORTC |= (1 << BLUE_LED);

    DDRB &= ~(1 << HEART_SENSOR);
}


int main(){
    pin_init();
    timers_init();
    while(1){}
}

void heart_state(){
    if(BPM < 60)
        PORTC = (1 << BLUE_LED);
    else if(BPM >= 60 && BPM <= 100)
        PORTC = (1 << GREEN_LED);
    if(BPM > 100)
        PORTC = (1 << RED_LED);
}

ISR(TIMER1_OVF_vect){
    BPM = round(60.0 * TCNT0 / TOTAL_OV1);
    heart_state();
    TCNT0 = 0;
    TCNT1 = 0;
}
