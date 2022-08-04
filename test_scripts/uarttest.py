import serial

serialport = serial.Serial("/dev/serial0", baudrate=9600)

while True:
    data = b'\x2A'
    serialport.write(data)
