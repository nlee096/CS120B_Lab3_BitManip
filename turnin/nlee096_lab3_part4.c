/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #4
 *	Exercise Description: take the upper nibble of PINA and map it to the lower nibble of PORTB, likewise take the lower nibble of PINA and map it to the upper nibble of PORTC
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
    DDRB = 0xFF; PORTB = 0x00;
    DDRC = 0xFF; PORTC = 0x00;

    unsigned char tmpA = 0x00;
    while(1)
    {
        tmpA = PINA;
        tmpA = tmpA & 0xF0;
        PORTB = tmpA >> 4;

        tmpA = PINA;
        tmpA = tmpA & 0x0F;
        PORTC = tmpA << 4;
    }
    return 1;
}
