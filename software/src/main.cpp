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
    Serial.begin(9600);//begin serial communication for GUI

    int counter;
    for(counter = 0; !Serial && counter < 2000; counter++){
        ;//Waiting for the Serial port to connect
    }
    if(counter == 2000)
        Serial.println("Serial port couldn't connect");
    else
        Serial.println("Serial port connected");

    Serial2.begin(9600);//begin serial communication for xbees

    for(counter = 0; !Serial2 && counter < 2000; counter++){
        ;//Waiting for the Serial2 port to connect
    }
    if(counter == 2000)
        Serial.println("Serial port couldn't connect");
    else
        Serial.println("Serial port connected");

}

void loop()
{
    while(Serial.available())
    {
        //read and send the logged data to the GUI
        if(Serial2.available() > 0)
        {
            String logData = Serial2.readString();
            Serial.println(logData);//sends transmitted data to the GUI
        }
        else
        {
            Serial.println("No data available");
        }

        //reads current state from the GUI, then executes some tasks accordingly
        uint8_t mode = Serial.read();
        State currState = (State) mode;
        String modeData = Serial.readString();
        if(Serial2.availableForWrite())
        {
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
        else
        {
            Serial.println("Couldn't write to xbees");
        }

    }

}