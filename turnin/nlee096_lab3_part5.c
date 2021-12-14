/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #5
 *	Exercise Description: car's passenger-seat weight sensor outputs a 9-bit value. airbag lights
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    DDRD = 0x00; PORTD = 0xFF;
    DDRB = 0xFE; PORTB = 0x00;

    unsigned short weight = 0x00;
    unsigned char tmpB = 0x00;
    unsigned char tmpC = 0x00;
    
    while(1)
    {
        weight =  ((short)PIND) << 1;
        if((PINB & 0x1) == 0x1){
            weight = weight | 0x1;
        }

        if(weight >= 0x46){
            tmpB = 0x02;
        }
        else if(weight <= 5){
            tmpB = 0x00;
        }
        else{
            tmpB = 0x04;
        }
        PORTB = tmpB;
    }
    return 1;
}
