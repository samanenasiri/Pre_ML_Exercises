
from string import ascii_lowercase, ascii_uppercase


def encrypt(plain_string,key):
    cipher_text=''
    ascii_uppercase
    for char in plain_string:
        cipher_num=ascii_uppercase.index(char)+ascii_uppercase.index(key)
        if cipher_num>25:
            cipher_num-=26
        cipher_text+=ascii_uppercase[cipher_num]
    return cipher_text
print(encrypt(input("text:").upper().replace(" ",""),input("key:").upper()))        

def decrypt(cipher_string,key):
    plain_text=''
    for char in cipher_string:
        plain_num=ascii_uppercase.index(char)-ascii_uppercase.index(key)
        if plain_num<0:
            plain_num+=26
        plain_text+=ascii_uppercase[plain_num]   
    return plain_text.lower() 
      
print(decrypt(input("cipher text:").upper(),input("key:").upper()))   


# print(decrypt(cipher_text,key)) 












            
# print(ascii_uppercase.index("B"))
# print(ascii_uppercase[2])
# print(len(ascii_uppercase))

# str_text="sa"
# for i in "ra":
#     str_text+=i
#     print(str_text)
# print(str_text)    
    
    