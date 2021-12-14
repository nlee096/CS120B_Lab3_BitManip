/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #1
 *	Exercise Description: Count the number of 1s on ports A and B and output that number on port C. 
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    DDRA = 0x00; PORTA = 0xFF;
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0xFF; PORTC = 0x00;
    unsigned char i;
    unsigned char cnt = 0x00;
    unsigned char mask = 0x01;
    while(1)
    {
        cnt = 0x00;
        mask = 0x01;
        for(i = 0; i < 8; i++){
            if((PINA & mask) > 0x00){
                cnt++;
            }
            mask = mask << 1;
        }

        mask = 0x01;
        for(i = 0; i < 8; i++){
            if((PINB & mask) > 0x00){
                cnt++;
            }
            mask = mask << 1;
        }
        PORTC = cnt;
    }
    return 1;
}
