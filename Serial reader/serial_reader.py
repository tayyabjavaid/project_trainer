import serial

# Code to write serial data into a CSV file
# format:
# AcX,AcY,AcZ,,<average_of_AcX_over_last_4_samples>,<average_of_AcY_over_last_4_samples>,<average_of_AcZ_over_last_4_samples>\n

ser = serial.Serial(port="COM1", timeout=None, baudrate=115200, xonxoff=False, rtscts=False, dsrdtr=False)
f = open("accell_data.csv", "w")
while True:
    data_raw = ser.readline()
    f.write(data_raw)
    print(data_raw)
