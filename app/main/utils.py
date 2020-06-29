def encrypt(text):
    text_list = list(text)
    
    encrypt_text = []

    for char in text_list:
        dec_code = ord(str(char))
        
        if 47 < dec_code < 58:
            dec_code -= 3
            char = chr(dec_code)
            encrypt_text.append(char)
        elif 64 < dec_code < 91:
            dec_code += 7
            char = chr(dec_code)
            encrypt_text.append(char)
        elif 96 < dec_code < 123:
            dec_code += 6
            char = chr(dec_code)
            encrypt_text.append(char)
    
    return ''.join(encrypt_text)

def decrypt(text):
    text_list = list(text)
    
    decrypt_text = []

    for char in text_list:
        dec_code = ord(str(char))
        
        if 44 < dec_code < 55:
            dec_code += 3
            char = chr(dec_code)
            decrypt_text.append(char)
        elif 71 < dec_code < 98:
            dec_code -= 7
            char = chr(dec_code)
            decrypt_text.append(char)
        elif 102 < dec_code < 129:
            dec_code -= 6
            char = chr(dec_code)
            decrypt_text.append(char)
    
    return ''.join(decrypt_text)

        

             
