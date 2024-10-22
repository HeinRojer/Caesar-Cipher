alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("welcome to Caesar Cipher")

print(''' ,             adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
            a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
            8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
            "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
             `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          
                                                                          ''')
print("""          88             88                                 
                   ""             88                                 
                                  88                                 
         ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
        a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
        8b         88 88       d8 88       88 8PP""""""" 88          
        "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
         `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                      88                                             
                      88                                             """)

def Caesar_Cypher():
    direction = input("Do you want to decrypt(Type decode)  or encrypt(Type encode)\n")
    shift = int(input("Enter the number of times you want to shift\n"))
    text = input("Enter the text you want to convert\n").lower()
    def encrypt(original_text , shift_amount):
        cipher_text = ""

        for i in original_text:
            if (i == " "):
                continue
            shifted_position = alpha.index(i)+shift_amount
            shifted_position %= len(alpha)
            cipher_text += alpha[shifted_position]
        print(f"The encoded text is : {cipher_text}")

    def decrypt(decode_text , shift_number):
        decoded_text = ""
        for i in decode_text:
            if( i == " " ):
                continue
            shift_position = alpha.index(i) - shift_number
            shift_position %= len(alpha)
            decoded_text += alpha[shift_position]
        print(f"The  decoded text is : {decoded_text}")

    if(direction == "encode"):
        encrypt(original_text = text , shift_amount = shift)
    elif direction == "decode":
        decrypt(decode_text = text, shift_number = shift )
    else:
        print("Invalid Input")
    print("Do You Want To Continue Again ")
    Repeat=input("Type yes for Again || Type no for Stoping\n").lower()
    if(Repeat == "yes"):
        print(Caesar_Cypher())
    else:
         print("Thank You For Using CAESAR CIPHER")
Caesar_Cypher()