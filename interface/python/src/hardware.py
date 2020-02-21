import serial
import serial.tools.list_ports


class device:
    ser = serial.Serial()

    # initialize
    def __init__(self):
        pass

    # delete and close port
    def __del__(self):
        self.disconnect()

    # helper to get the port with MCU connected
    def __getMcuPort(self, strName):
        ports = list(self.__getPorts())
        num = len(ports)
        ret = "NONE"
        for p in range(0, num):
            port = str(ports[p])
            if port.find(strName) is not -1:
                ret = port.split(' ')[0]
                ret = ret[ret.find("\'")+1:ret.find("\'", 3)]
        return ret

    # helper to return list of com ports
    def __getPorts(self):
        ports = serial.tools.list_ports.comports()
        return ports

    # connects to connected mcu
    def serialConnect(self, strName="USB"):
        port = self.__getMcuPort(strName)
        if port is not "NONE":
            self.ser.port = port
            self.ser.timeout = 0
            self.setBaudRate(9600)
            self.ser.open()
            print("connected")
        else:
            # handle error here
            print("Error: No Arduino Connected")

    # sets baud rate for serial connection
    def setBaudRate(self, newRate):
        self.br = newRate
        self.ser.baudrate = newRate

    # returns baud rate of serial connection
    def getBaudRate(self):
        if self.isConnected():
            return self.ser.baudrate
        else:
            return 0

    # retruns true true if connected, false if disconnected
    def isConnected(self):
        return self.ser.isOpen()

    # closes serial port communications
    def disconnect(self):
        self.ser.close()

    # returns string of line read from from serial port
    def readLine(self):
        line = self.ser.readline()
        return str(line.strip().decode('ascii'))

    def write(self, data):
        if (self.ser.writable()):
            self.ser.write(str(data).encode('UTF-8'))
        else:
            return 0
