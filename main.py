def asd_request(cmd,subcmd,length,ident,data):

    request_int = [cmd, subcmd, length, ident]
    checksum = cmd ^ subcmd ^ length ^ ident

    for i in data:
        checksum ^ i
        request_int.append(i)

    request_int.append(checksum)
                                   
    return request_int


if __name__ == "__main__":                                      
    import serial

    ser = serial.Serial(port = 'COM1',timeout = 0, baudrate=19200,bytesize=8,parity="N",stopbits=1)
    

    ser.write(asd_request(cmd = 2, subcmd = 3, length = 5, ident = 1, data = []))

    asd_answer = ser.read(61)
    

    if len(asd_answer) > 0:
        if asd_answer[5] == 0x00:
            airflow_current_1 = asd_answer[15]
            airflow_current_2 = asd_answer[16]
            airflow_fault_1 = asd_answer[17]
            airflow_fault_2 = asd_answer[18]

            print("airflow_current_1",airflow_current_1)
            print("airflow_current_2", airflow_current_2)
            print("airflow_fault_1",airflow_fault_1)
            print("airflow_fault_2",airflow_fault_2)
        else:
            print("ERROR: ", asd_answer[5])
    else:
        print("empty")

    ser.close()
    
    

