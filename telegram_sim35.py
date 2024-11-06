import serial
import serial.rs485
import argparse
from redundancy import modbusCrc

parser = argparse.ArgumentParser(allow_abbrev=True)
parser.add_argument('--sfd',type=int, default = 1)
#parser.add_argument('--tgm',type=int, default = 3)
parser.add_argument('--cmd',type=int, default = 5)
parser.add_argument('--info',type=int, default = 1)
parser.add_argument('--data', type=bytearray, default = b'')

parser.add_argument('--port',type=str, default = 'COM1')
parser.add_argument('--answer-length',type=int, default = 134)
args = parser.parse_args()

ser = serial.Serial(args.port, timeout = 0, baudrate=19200, bytesize=8, parity="N", stopbits=1)
ser_2 = serial.Serial(port='COM2', timeout = 0, baudrate=19200, bytesize=8, parity="N", stopbits=1)

tgm = len(args.data) + 6
request = bytearray([args.sfd, tgm, args.cmd, args.info])
for i in args.data:
    request.append(int(i))
    
crcl, crch = modbusCrc(bytes.fromhex("0104080000000900000000"))

request.append(crcl)
request.append(crch)

ser.write(request)

asd_answer = ser_2.read(args.answer_length)

print("complete: ", asd_answer)

ser.close()


    

