#include <Arduino.h>

#define xbeepin1 1
#define xbeepin2 2

#define xbeeFreq 123456789

typedef enum {
   StartUp,
   Ready,
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
        if(Serial2.available() > 0)
        {
            String logData = Serial2.read();
            Serial.println(logData);//sends transmitted data to the GUI
        }
        else
        {
            Serial.println("No data available");
        }

        //reads current state from the GUI, then executes some tasks accordingly
        if(Serial.available() > 0)
        {
            uint8_t mode = Serial.read();
            State currState = (State) mode;
            String modeData = Serial.readString();
            switch(currState){
                case Ready:{
                    //Serial2.println(mode + "," + modeData);
                    Serial2.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
                    break;
                }
                case StartUp:{
                    //Serial2.println(mode + "," + modeData);
                    Serial2.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
                    break;
                }
                case Flight:{
                    Serial.println("Cannot enter flight mode through the ground control!!");
                    break;
                }
                default:
                    Serial.println("You sent the wrong state!!");
            }
        }

    }

}