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
    Serial.begin(9600);//begin serial communication for GUI
    delay(3000);

    Serial1.begin(9600);
    delay(3000);

    pinMode(ledStat, OUTPUT);
    pinMode(ledStat2, OUTPUT);

    /*
    int counter;
    for(counter = 0; !Serial && counter < 2000; counter++){
        ;//Waiting for the Serial port to connect
    }
    if(counter == 2000)
        Serial.println("Serial port couldn't connect");
    else
        Serial.println("Serial port connected");

    Serial4.begin(9600);//begin serial communication for xbees

    for(counter = 0; !Serial4 && counter < 2000; counter++){
        ;//Waiting for the Serial4 port to connect
    }
    if(counter == 2000)
        Serial.println("Serial port couldn't connect");
    else
        Serial.println("Serial port connected");
    */
}

void loop()
{
        char logData;
        //Serial.println("At main loop");
        //Serial.println("Got here");
        //read and send the logged data to the GUI
        while(Serial1.available())
        {
            //String logData = Serial1.readStringUntil('\n');
            logData = Serial1.read();
            Serial.print(logData);//sends transmitted data to the GUI
        }

        /*
        if(!Serial1.available())
        {
            delay(1000);
            digitalWrite(ledStat2, HIGH);
            delay(1000);
            digitalWrite(ledStat, LOW);
        }
        */
        /*
        if(Serial1.available() > 0)
        {
            //Serial.print("Serial 4 Available. Data: ");
            //digitalWrite(ledStat, HIGH);
            String logData = Serial1.readStringUntil('\n');
            //String logData = Serial4.readString();
            Serial.println(logData);//sends transmitted data to the GUI
            //delay(1000);
            //digitalWrite(ledStat, LOW);
        }
        else
        {
            delay(1000);
            digitalWrite(ledStat2, HIGH);
            delay(1000);
            digitalWrite(ledStat, LOW);
            //Serial.println("No data available");
        }
        */
        //delay(1000);

        /*
        //reads current state from the GUI, then executes some tasks accordingly
        uint8_t mode = Serial.read();
        State currState = (State) mode;
        String modeData = Serial.readString();
        if(Serial4.availableForWrite())
        {
            switch(currState){
            case Ready:{
                //Serial4.println(mode + "," + modeData);
                Serial4.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
                break;
            }
            case StartUp:{
                //Serial4.println(mode + "," + modeData);
                Serial4.printf("%d,%s\n", mode, modeData);//sending the mode to the xbee for transmission
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
        */

}