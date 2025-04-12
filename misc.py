
# 看了半天发现是9键加密
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

# 这里是拆分pem证书的函数
def pem(data):
    from base64 import b64decode
    new_data = ''
    for i in data.split('\n'):
        if '-----' in i:
            pass
        else:
            new_data += i
    return b64decode(new_data)

# 凯撒解密的工具函数与调用函数
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text

def caesar(ciphertext, shift_keyword=''):
    if type(shift_keyword) == str:
        for i in range(26):
            decrypted_text = caesar_decrypt(ciphertext, i)
            if shift_keyword in decrypted_text:
                print(f'shift {i}: {decrypted_text}')
    else:
        print(caesar_decrypt(ciphertext, shift_keyword))
    
# 维吉尼亚解密的工具函数与调用函数
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value_base = ord('A') if ciphertext[i].isupper() else ord('a')
            key_value_base = ord('A') if key[i % key_length].isupper() else ord('a')
            decrypted_value = (ciphertext_int[i] - value_base - 
                               (key_as_int[i % key_length] - key_value_base)) % 26 + value_base
            decrypted_text.append(chr(decrypted_value))
        else:
            decrypted_text.append(ciphertext[i])
    return ''.join(decrypted_text)

def vigenere_findkey(ciphertext, key, length=0):
    decrypted_text = []
    key_length = len(key)
    length = key_length if length == 0 else length
    print(length)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext[:length]]
        
    
    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value_base = ord('A') if ciphertext[i].isupper() else ord('a')
            key_value_base = ord('A') if key[i % key_length].isupper() else ord('a')
            decrypted_value = (ciphertext_int[i] - value_base - 
                               (key_as_int[i % key_length] - key_value_base)) % 26 + value_base
            decrypted_text.append(chr(decrypted_value))
        else:
            decrypted_text.append(ciphertext[i])
    return ''.join(decrypted_text)

def vigenere(ciphertext, key, length=0):
    key = vigenere_findkey(ciphertext, key, length)
    msg = vigenere_decrypt(ciphertext, key)
    print(msg)
    return msg

