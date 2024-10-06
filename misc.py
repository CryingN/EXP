
def nine_key(in_data, UP = False):
    in_data = str(in_data)
    out_data = ""
    for i in range(0, len(in_data), 2):
        if int(in_data[i]) == 2 and int(in_data[i+1]) == 1:out_data += "a"
        elif int(in_data[i]) == 2 and int(in_data[i+1]) == 2:out_data += "b"
        elif int(in_data[i]) == 2 and int(in_data[i+1]) == 3:out_data += "c"
        elif int(in_data[i]) == 3 and int(in_data[i+1]) == 1:out_data += "d"
        elif int(in_data[i]) == 3 and int(in_data[i+1]) == 2:out_data += "e"
        elif int(in_data[i]) == 3 and int(in_data[i+1]) == 3:out_data += "f"
        elif int(in_data[i]) == 4 and int(in_data[i+1]) == 1:out_data += "g"
        elif int(in_data[i]) == 4 and int(in_data[i+1]) == 2:out_data += "h"
        elif int(in_data[i]) == 4 and int(in_data[i+1]) == 3:out_data += "i"
        elif int(in_data[i]) == 5 and int(in_data[i+1]) == 1:out_data += "j"
        elif int(in_data[i]) == 5 and int(in_data[i+1]) == 2:out_data += "k"
        elif int(in_data[i]) == 5 and int(in_data[i+1]) == 3:out_data += "l"
        elif int(in_data[i]) == 6 and int(in_data[i+1]) == 1:out_data += "m"
        elif int(in_data[i]) == 6 and int(in_data[i+1]) == 2:out_data += "n"
        elif int(in_data[i]) == 6 and int(in_data[i+1]) == 3:out_data += "o"
        elif int(in_data[i]) == 7 and int(in_data[i+1]) == 1:out_data += "p"
        elif int(in_data[i]) == 7 and int(in_data[i+1]) == 2:out_data += "q"
        elif int(in_data[i]) == 7 and int(in_data[i+1]) == 3:out_data += "r"
        elif int(in_data[i]) == 7 and int(in_data[i+1]) == 4:out_data += "s"
        elif int(in_data[i]) == 8 and int(in_data[i+1]) == 1:out_data += "t"
        elif int(in_data[i]) == 8 and int(in_data[i+1]) == 2:out_data += "u"
        elif int(in_data[i]) == 8 and int(in_data[i+1]) == 3:out_data += "v"
        elif int(in_data[i]) == 9 and int(in_data[i+1]) == 1:out_data += "w"
        elif int(in_data[i]) == 9 and int(in_data[i+1]) == 2:out_data += "x"
        elif int(in_data[i]) == 9 and int(in_data[i+1]) == 3:out_data += "y"
        elif int(in_data[i]) == 9 and int(in_data[i+1]) == 4:out_data += "z"
    if UP:
        out_data = out_data.upper()
    return out_data



