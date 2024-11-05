import serial


ser = serial.Serial(port='COM3',baudrate=19200,bytesize=8,parity="N",stopbits=1)

cmd = 2
subcmd = 3
length = 5
ident = 1
data0 = 0

checksum = cmd ^ subcmd ^ length ^ ident ^ data0
request = [cmd, subcmd, length, ident, data0, checksum]

ser.write(request)