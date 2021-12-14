/*	Author: Nathan Lee nlee096@ucr.edu
 *  Partner(s) Name: none
 *	Lab Section: 022
 *	Assignment: Lab #3  Exercise #3
 *	Exercise Description: Fuel level sensor + seatbelt light
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
    DDRC = 0xFF; PORTC = 0x00;
    
    unsigned char temp_out = 0x00;
    unsigned char tmpA = 0x00;

    while(1)
    {
        temp_out = 0x00;
        tmpA = PINA & 0x0F;
        switch(tmpA){
            case 15 :
            case 14 :
            case 13 :
                temp_out = temp_out | 0x01;

            case 12 :
            case 11 :
            case 10 :
                temp_out = temp_out | 0x02;

            case 9 :
            case 8 :
            case 7 :
                temp_out = temp_out | 0x04;

            case 6 :
            case 5 :
                temp_out = temp_out | 0x08;

            case 4 :
            case 3 :
                temp_out = temp_out | 0x10;

            case 2 :
            case 1 :
                temp_out = temp_out | 0x20;

            case 0 :
            default:
                if(tmpA < 5){
                    temp_out = temp_out | 0x40;
                }
            break;
        }
        
        tmpA = PINA & 0x70;
        if(tmpA == 0x30){
            temp_out = temp_out | 0x80;
        }
        PORTC = temp_out;
    }
    return 1;
}
