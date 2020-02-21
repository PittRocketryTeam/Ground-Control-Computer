#include <Arduino.h>

#define ledStat 36
#define ledStat2 38

typedef enum {
   StartUp,
   Ready,
   Flight
} State;

void setup()
{
    Serial.begin(9600);//begin serial communication for the serial monitor
    while(!Serial)
    {
        ;//wait until Serial connects
    }
    Serial.println("Serial connection opened");

    Serial1.begin(9600);//begin serial connunication for the Xbee 
    while(!Serial1)
    {
        ;//wait until Serial1 connects
    }
    Serial.println("Serial 1 connection opened");

    Serial2.begin(9600);//begin serial connunication for the GUI
    while(!Serial2)
    {
        ;//wait until Serial2 connects
    }
    Serial.println("Serial 2 connection opened");
}

void loop()
{
    char mode;
    String logData, modeData;
    uint8_t changedMode;
    
    if(Serial1.available())//if statement b/c the entire thing is already in a loop. Will allow the mode to be changed during reading
    {
        logData = Serial1.readStringUntil('\n');
        //logData += "\n";
        if(logData != "")
        {
            Serial.println(logData);//sends the logged data from SCA to the GUI. Should be sending a zero terminator then new line at the end
        }
        logData = "";
    }
    
    //if(Serial2.available())//reads current state from the GUI, then executes some tasks accordingly
    if(Serial2.available())
    {
        //mode = Serial2.read();
        mode = 1;
        State currState = (State) mode;
        modeData = "hi";
        //modeData = Serial2.readStringUntil('\0');

        switch(currState){
            case Ready:{
                Serial1.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
                break;
            }
            case StartUp:{
                Serial1.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
                break;
            }
            case Flight:{
                Serial.println("Cannot enter flight mode through the ground control!!");
                break;
            }
            default:{
                Serial.println("You sent the wrong state!!");
            }
        }
    }

}