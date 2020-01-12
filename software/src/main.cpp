#include <Arduino.h>

#define xbeepin1 1
#define xbeepin2 2

#define xbeeFreq 123456789

void setup()
{
    Serial.begin(9600);

    while(!Serial){
        ;//Waiting for the Serial port to connect
    }

    Serial.println("Serial port connected");
    //print something to the ground control saying that connection has been established

    // put your setup code here, to run once:
}

void loop()
{
    while(Serial.available())
    {
        //char[] = xbee.receive();
        /*
        * Recieve SCA data from Xbee
        *   Send that data to the ground control
        * See if there's a command to send
        *   if there's a command, send it to SCA via xbee
        */
    }
    // put your main code here, to run repeatedly:
}