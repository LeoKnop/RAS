import serial
import argparse
from redundancy import checksum_calc

parser = argparse.ArgumentParser(allow_abbrev=True)
parser.add_argument('--cmd',type=int, default = 2)
parser.add_argument('--subcmd',type=int, default = 3)
#parser.add_argument('--length',type=int, default = 5)
parser.add_argument('--ident',type=int, default = 1)
parser.add_argument('--data', nargs='+', default = [])

parser.add_argument('--port',type=str, default = 'COM1')
parser.add_argument('--answer-length',type=int, default = 61)
args = parser.parse_args()

ser = serial.Serial(args.port, timeout = 0, baudrate=19200, bytesize=8, parity="N", stopbits=1)
ser_2 = serial.Serial(port='COM2', timeout = 0, baudrate=19200, bytesize=8, parity="N", stopbits=1)

length = 5 + len(args.data)
request = bytearray([args.cmd, args.subcmd, length, args.ident])
for i in args.data:
    request.append(int(i))

checksum = checksum_calc(args.cmd, args.subcmd, length, args.ident, args.data)
request.append(checksum)

ser.write(request)

asd_answer = ser_2.read(args.answer_length)

print("complete: ", asd_answer)

if len(asd_answer) > 0:
    '''
    if asd_answer[5] == 0x00:
        airflow_current_1 = asd_answer[15]
        airflow_current_2 = asd_answer[16]
        airflow_fault_1 = asd_answer[17]
        airflow_fault_2 = asd_answer[18]

        print("airflow_current_1",airflow_current_1)
        print("airflow_current_2", airflow_current_2)
        print("airflow_fault_1",airflow_fault_1)
        print("airflow_fault_2",airflow_fault_2)
        print("complete", asd_answer)
    else:
        print("ERROR: ", asd_answer[5])
    '''
else:
    print("empty")
ser.close()


    

