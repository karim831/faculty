#include<avr/io.h>
#include<avr/interrupt.h>
#include<math.h>

#define F_CPU 8000000

#define P_SCALAR1 256
#define TIC_TIME1 ((P_SCALAR1 * 1.0) / F_CPU)
#define TCCR1B_SETUP ((1 << ICES1) | (1 << CS12))
#define TIMSK_TIMER1_SETUP (1 << TICIE1)

#define P_SCALAR0 1024
#define TIC_TIME0 ((P_SCALAR0 * 1.0) / F_CPU) 
#define TCCR0_SETUP (1 << CS02)
#define SW_COUNTER 122 // 1 second
#define TIMSK_TIMER0_SETUP (1 << TOIE0)


#define BLUE_LED PC0
#define GREEN_LED PC1
#define RED_LED PC2
#define ICP_PIN PD6


uint16_t prev_counter = 0;
uint8_t BPM = 0;

uint8_t sw_counter = SW_COUNTER;

void timer1_pulse_measurement_init(){
    TCCR1B = 0;
    TCNT1 = 0;
    ICR1 = 0;

    TIMSK |= TIMSK_TIMER1_SETUP;
    TCCR1B |= TCCR1B_SETUP;
}

void timer0_heart_status_leds_tracker_init(){
    TCCR0 = 0;
    TCNT0 = 0;

    TIMSK |= TIMSK_TIMER0_SETUP;
    TCCR0 |= TCCR0_SETUP;
}

void timers_init(){
    timer0_heart_status_leds_tracker_init();
    timer1_pulse_measurement_init();
    sei();
}

void pin_init(){
    DDRC |= (1 << BLUE_LED) | (1 << GREEN_LED) | (1 << RED_LED);
    PORTC |= (1 << BLUE_LED);

    DDRD &= ~(1 << ICP_PIN);
}


int main(){
    pin_init();
    timers_init();
    while(1){}
}


ISR(TIMER1_CAPT_vect){
    uint16_t curr_counter = ICR1;
    if(!(prev_counter))
        prev_counter = curr_counter;
    else{
        uint16_t diff = curr_counter - prev_counter;
        BPM =  round((60.0 / (diff * TIC_TIME1)));
        prev_counter = 0;
    }
}

ISR(TIMER0_OVF_vect){
    if(!sw_counter){
        if(BPM < 50)
            PORTC = (1 << BLUE_LED);
        else if(BPM >= 50 && BPM < 100)
            PORTC = (1 << GREEN_LED);
        if(BPM >= 100)
            PORTC = (1 << RED_LED);
        
        sw_counter = SW_COUNTER;
    }
    sw_counter--;
}