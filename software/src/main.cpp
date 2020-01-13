#include <Arduino.h>

#define xbeepin1 1
#define xbeepin2 2

#define xbeeFreq 123456789

typedef enum {
   PreLaunch,
   OnPad,
   Flight
} State;

void setup()
{
    Serial.begin(9600);//begin serial communication

    while(!Serial){
        ;//Waiting for the Serial port to connect
    }
    Serial.println("Serial port connected");

}

void loop()
{
    while(Serial.available())
    {
        //read and send the logged data to the GUI
        char data[] = "No data available";
        //data = xbee.receive();
        Serial.println(data);//sends transmitted data to the GUI

        //reads current state from the GUI, then executes some tasks accordingly
        State currState = (State)Serial.read();
        switch(currState){
            case PreLaunch:{
                break;//do stuff during pre-launch
            }
            case OnPad:{
                break;//do stuff that we'd do while sitting on the pad before flight
            }
            case Flight:{
                break;//operate in flight mode here
            }
            default:
                Serial.println("You sent the wrong state!!");
        }

        /*
        * Recieve SCA data from Xbee
        *   Send that data to the ground control
        * See if there's a command to send
        *   if there's a command, send it to SCA via xbee
        */
    }

}