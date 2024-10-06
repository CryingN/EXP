
def get_data(data):
    if "0x" == data[0:2]:
        data = data[2:]
    new_data = ""
    for i in range(0, len(data), 2):
        new_data += chr(int(data[i:i+2],16))
    return new_data[::-1]


