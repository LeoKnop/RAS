def checksum_calc(cmd,subcmd,length,ident,data):
    checksum = cmd ^ subcmd ^ length ^ ident
    for i in data:
        checksum = checksum ^ int(i)
    return checksum

def modbusCrc(data):
    crc = 0xFFFF
    for n in range(len(data)):
        crc ^= data[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    ba = crc.to_bytes(2, byteorder='little')
    return ba[0], ba[1]


